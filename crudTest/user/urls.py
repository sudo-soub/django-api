from django.urls import path
from user import views

urlpatterns = [
    path('api/user/login', views.login),
]
