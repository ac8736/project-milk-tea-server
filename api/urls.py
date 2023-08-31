from django.urls import path
from . import views

urlpatterns = [
    path('', views.getData),
    path('test', views.test),
    path('add-link', views.addLink),
]