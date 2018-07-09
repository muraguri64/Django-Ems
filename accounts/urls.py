from django.contrib import admin
from django.urls import path
from . import views

from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete

urlpatterns = [
    path('signup/', views.signup, name='accounts_signup'),
    path('login/', views.login, name='accounts_login'),
    path('logout/', views.logout, name='accounts_logout'),
    #for password resets

    path('reset-password/', password_reset,{'template_name': 'accounts/password_reset.html'}, name='reset_password'),
    path('reset-password/done/', password_reset_done, {'template_name': 'accounts/password_reset_done.html'}, name='password_reset_done'),
    path('reset-password/confirm/?P<uidb64>[0-9A-Za-z]+-?P<token>/', password_reset_confirm, {'template_name': 'accounts/password_reset_confirm.html'},name='password_reset_confirm'),
    path('reset-password/complete/', password_reset_complete, {'template_name': 'accounts/password_reset_complete.html'},  name='password_reset_complete'),


]
