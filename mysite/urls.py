from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home),
    path('about/', views.about),
    path('services/', views.services),
    path('contactus/', views.contactus),
]