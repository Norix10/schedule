from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_render, name='lesson_list'),
]