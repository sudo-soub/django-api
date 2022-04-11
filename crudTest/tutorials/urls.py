from django.urls import path
from tutorials import views

urlpatterns = [
    path('all', views.tutorial_list),
    path('<int:pk>', views.tutorial_detail),
    path('published', views.tutorial_list_published),
    path('user/<int:userid>', views.tutorialforuser),
    path('getavailabletutorialslist', views.availabletutorials)
]
