from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homeS'),
    path('login/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('add-instructor/', views.add_instructor, name='add_instructor'),
    path('add-course/', views.add_course, name='add_course'),
    path('schedule-lecture/', views.schedule_lecture, name='schedule_lecture'),
    path('instructor-dashboard/', views.instructor_dashboard, name='instructor_dashboard'),
]
