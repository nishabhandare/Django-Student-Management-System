from django.urls import path
from . import views

urlpatterns = [

    path('', views.view_students, name='view_students'),

    path('add/', views.add_student, name='add_student'),

    path('update/<int:id>/', views.update_student, name='update_student'),

    path('delete/<int:id>/', views.delete_student, name='delete_student'),

    path('student/<int:id>/', views.view_student, name='view_student'), 
    
    path('search/', views.search_student, name='search_student'),
    ]
    
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]


urlpatterns = [
    path('', views.student_list, name='student_list'),
]