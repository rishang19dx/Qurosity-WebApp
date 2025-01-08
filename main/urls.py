from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('events/', views.events, name='events'),
    path('trivia/', views.trivia, name='trivia'),
    path('team/', views.team, name='team'),
    path('contact/', views.contact, name='contact'),
]
