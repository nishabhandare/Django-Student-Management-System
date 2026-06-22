from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from Students import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # 🔐 Authentication paths
    # 'students/login.html' काढून फक्त 'login.html' करा
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    # 📁 Student Management System Paths (थेट मुख्य रूट वर जोडले आहेत)
    path('', views.view_students, name='view_students'),
    path('add/', views.add_student, name='add_student'),
    path('update/<int:id>/', views.update_student, name='update_student'),
    path('delete/<int:id>/', views.delete_student, name='delete_student'),
    path('student/<int:id>/', views.view_student, name='view_student'), 
    path('search/', views.search_student, name='search_student'),
    
    # जर भविष्यात ॲप लेव्हल urls वापरायचे असतील तर:
    path('Students/', include('Students.urls')),
]