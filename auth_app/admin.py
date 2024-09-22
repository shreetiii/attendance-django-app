from django.contrib import admin
from .models import Teacher, Student, Course

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['user','address','primary_number','secondary_number','sex']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name','address','phone_number','age']

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = [
        'teacher',
        'duration',
        'shift',
        'title'
    ]