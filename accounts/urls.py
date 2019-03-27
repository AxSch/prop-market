from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
  path('login', auth_views.LoginView.as_view(template_name='accounts/login.html', redirect_authenticated_user=True), name='login'),
  path('register', views.register, name='register'),
  path('logout', views.logout, name='logout'),
  path('dashboard', views.dashboard, name='dashboard'),
]