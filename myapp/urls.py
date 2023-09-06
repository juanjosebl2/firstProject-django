from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home),
    path('about/', views.About),
    path('hello/<str:username>', views.Hello),
    path('projects/', views.projects),
    path('tasks/<int:id>', views.tasks),
]