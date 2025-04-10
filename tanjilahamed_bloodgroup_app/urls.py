from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home),
    path('insert', views.add, name="insert"),
    path('view', views.display, name="view"),
]