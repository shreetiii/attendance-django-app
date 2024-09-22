from django.shortcuts import render
from auth_app.models import Teacher, Course
from django.shortcuts import redirect
from .forms import ImageForm, TeacherEditForm
from auth_app.models import StudentClass, Attendance
from django.contrib import messages

import os 
from django.conf import settings
from django.core.files.storage import default_storage
from datetime import date, timedelta
import calendar

# Create your views here.

def course_list(request):
    print("Course List")
    print(request.user.id)
    user_id = request.user.id
    teacher = Teacher.objects.get(user=user_id)
    list_of_courses = Course.objects.filter(teacher=teacher).prefetch_related('teacher')
    print(list_of_courses)
    return render(request, 'attendance/course_list.html',{'courses':list_of_courses})

def profile(request):
    user_id = request.user.id
    teacher = Teacher.objects.get(user=user_id)
    list_of_courses = Course.objects.filter(teacher=teacher).prefetch_related('teacher')

    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            print("Form is valid")
            print(form.cleaned_data)
            teacher.image = form.cleaned_data['image']
            teacher.save()
        else: 
            print(form.errors)
    else:
        form = ImageForm()
    return render(request, 'attendance/profile.html',{'courses':list_of_courses,'teacher':teacher,'form':form})

def remove_image(request):
    user_id = request.user.id
    teacher = Teacher.objects.get(user=user_id)
    if teacher.image and teacher.image.name != 'NA':
        image_path = os.path.join(settings.MEDIA_ROOT, teacher.image.name)
        print("Image Path")
        print(image_path)
        if default_storage.exists(image_path):
            default_storage.delete(image_path)
            teacher.image = 'NA'
            teacher.save()
    return redirect('profile')

def edit_profile(request):
    user_id = request.user.id
    teacher = Teacher.objects.get(user=user_id)

    if request.method == "POST":
        post_data = request.POST.copy()
        print(post_data)
        post_data['sex'] = teacher.sex
        post_data['dob'] = teacher.dob
        print(post_data)
        form = TeacherEditForm(post_data,instance=teacher)
        if form.is_valid():
            print("Form is Saved")
            form.save()
        else: 
            print(form.errors)

    form = TeacherEditForm(instance=teacher)

    return render(request,'attendance/edit-profile.html',{
        'form':form,
        'teacher':teacher
    })

# Calender Views

def display_calendar(request,id):
    request.session['course_id'] = id
    todays_date = date.today()
    year = todays_date.year
    this_month = todays_date.month
    day = todays_date.day

    cal = calendar.Calendar()
    cal.setfirstweekday(6)
    month_name = calendar.month_name[todays_date.month]
    print(month_name)
    print(todays_date)
    cal_days = list(cal.itermonthdays(year,this_month))
    print(cal_days)
    return render(request,'attendance/calendar.html',{'cal_days':cal_days,'month_name':month_name,'today_date':todays_date})

def choose_date(request):
    # Attendance.objects.all().delete()
    course_id = request.session.get('course_id')
    print("Course ID",course_id)
    course_obj = Course.objects.get(id=course_id)
    todays_date = date.today()
    month_name = calendar.month_name[todays_date.month]

    students = StudentClass.objects.prefetch_related('student').filter(course=course_id)

    past_date = [todays_date - timedelta(days=i) for i in range(1,8)]

    print(past_date)

    if request.method == "POST":
        print(request.POST)
        for item in students:
            student_id = item.student.id
            status = request.POST.get(str(student_id))
            Attendance.objects.create(
                today_date=todays_date - timedelta(days=5),
                student_id=student_id,
                course_id=course_id,
                stats=status
            )
        
        messages.success(request,f'Attendance has been marked successfully for {course_obj.title}') 
        return redirect('course-list')
    
    else: 
        year = todays_date.year
        this_month = todays_date.month
    
    status_dict = {}

    for item in students:
        student_id = item.student.id
        status_dict[student_id] = {}
        for i in past_date:
            try:
                obj = Attendance.objects.get(today_date=i,student=student_id,course=course_id)
                status_dict[student_id][i.day] = obj.stats
            except Attendance.DoesNotExist:
                status_dict[student_id][i.day] = 'NA'
    print("Status Dict")
    print("\n")
    print(status_dict)

    return render(request,'calendar/student_list.html',{'month_name':month_name,'today_date':todays_date,'students':students,'past_date':past_date,'status_dict':status_dict})