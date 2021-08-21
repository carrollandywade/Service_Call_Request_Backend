from django.urls import path
from . import views

urlpatterns = [
    path('callrouting/', views.CustomerList.as_view()),
]
