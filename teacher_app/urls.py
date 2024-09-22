from django.urls import path
from . import views

urlpatterns = [
    path('course-list/', views.course_list, name='course-list'),
    path('profile/', views.profile, name='profile'),
    path('remove-image/', views.remove_image, name='remove-image'),
    path('edit-profile/', views.edit_profile, name='edit-profile'),
    
    # Calendar Paths
    path('calendar/<int:id>', views.display_calendar, name='calendar'),
    path('choose_date/', views.choose_date, name='choose-date'),

]