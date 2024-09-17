from django.urls import path
from auth_app import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.login_page, name='login'),
    path('admin-page/', views.admin_view, name='admin-page-name'),
    path('logout/', views.logout_user  , name='logout'),
    path('register/', views.register_user, name='register'),
    path('teacher/', views.teacher, name='teacher'),
    path('image/', views.teacher_image, name='image'),
    path('student/', views.add_student, name='add-student'),



]
