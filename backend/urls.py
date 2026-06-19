from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    # Students
    path('student/add/', views.add_student, name='add_student'),
    path('student/edit/<int:id>/', views.edit_student, name='edit_student'),
    path('student/delete/<int:id>/', views.delete_student, name='delete_student'),

    # Subjects
    path('subject/add/', views.add_subject, name='add_subject'),
    path('subject/edit/<int:id>/', views.edit_subject, name='edit_subject'),
    path('subject/delete/<int:id>/', views.delete_subject, name='delete_subject'),

    # Teachers
    path('teacher/add/', views.add_teacher, name='add_teacher'),
    path('teacher/edit/<int:id>/', views.edit_teacher, name='edit_teacher'),
    path('teacher/delete/<int:id>/', views.delete_teacher, name='delete_teacher'),
]