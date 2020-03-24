from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.indexView, name='index'),
    path('update_task/<str:pk>/', views.updateView, name='update_task'),
    path('delete_task/<str:pk>/', views.deleteView, name='delete_task'),
    path('complete_task/<str:pk>/', views.completeView, name='complete_task'),
    path('un_complete_task/<str:pk>/',
         views.un_completeView, name='un_complete_task'),
]
