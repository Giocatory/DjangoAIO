from django.urls import path
from . import views


urlpatterns = [
    path('', views.energo, name='energo'),
]
