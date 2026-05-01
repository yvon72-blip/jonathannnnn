from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/toggle-like/', views.toggle_like, name='toggle_like'),
]
