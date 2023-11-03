from django.urls import path
from . import views


urlpatterns = [
    path('', views.ikibzyak, name='ikibzyak'),
]
