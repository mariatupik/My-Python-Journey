from django.urls import path
from django.contrib.auth import views as auth_views # Не забудьте додати цей імпорт
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('add-course/', views.CourseAdd.as_view(), name='course_add'),
    path('course/<slug:slug>/', views.CourseDetailPage.as_view(), name='course_detail'),
    path('course/<slug:slug>/lesson/<slug:lesson_slug>/', views.LessonDetailPage.as_view(), name='lesson_detail'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('accounts/profile/', views.profile, name='profile_alias'),
    path('course/<slug:slug>/delete/', views.CourseDeleteView.as_view(), name='course_delete'),
    path('login/', auth_views.LoginView.as_view(template_name='courses/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]