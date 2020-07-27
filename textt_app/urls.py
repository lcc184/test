from django.urls import path
from textt_app import views
urlpatterns = [
    path('index/', views.index),
]
