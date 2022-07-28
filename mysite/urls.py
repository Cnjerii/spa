from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', views.Home),
    path('about/', views.about),
    path('services/', views.services),
    path('contactus/', views.contactus),
]

urlpatterns += staticfiles_urlpatterns()