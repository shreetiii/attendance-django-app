from django.contrib import admin
from django.urls import path
from auth_app import views

urlpatterns = [
    path('', views.login_page, name='login'),
    path('admin-page/', views.admin_view, name='admin-page-name'),
    path('logout/', views.logout_user  , name='logout'),
    path('register/', views.register_user, name='register'),

]
