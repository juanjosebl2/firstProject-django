from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home),
    path('about/', views.About),
    path('hello/<str:username>', views.Hello),
]