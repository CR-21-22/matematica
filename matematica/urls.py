from django.urls import path

from matematica import views

urlpatterns = [
    path('', views.index)
]