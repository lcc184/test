from django.urls import path
from bug_app import views
urlpatterns = [
    path('index/', views.index),
]
