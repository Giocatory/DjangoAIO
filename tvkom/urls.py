from django.urls import path
from . import views


urlpatterns = [
    path('', views.tvkom, name='tvkom'),
]
