from django.urls import path

from user import views

app_name = 'user'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('login_logic/', views.login_logic, name='login_logic'),
    path('register/', views.register, name='register'),
    path('register_logic/', views.register_logic, name='register_logic'),
    path('get_captcha/', views.get_captcha, name='get_captcha'),
    path('log_out/', views.log_out, name='log_out'),
    path('get_username/', views.get_username, name='get_username'),
    path('get_code', views.get_code, name='get_code'),
]
