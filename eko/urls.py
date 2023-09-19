from django.urls import path
from . import views


urlpatterns = [
    path('', views.eko, name='eko'),
]
