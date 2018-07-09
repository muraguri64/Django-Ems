from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='polls_index'),
    path('<int:id>/details/', views.details, name='poll_details'),
    path('poll/<int:id>/answer', views.poll, name='poll_answer')
]
