from django.urls import path
from . import views


urlpatterns = [
    path('', views.energo, name='energo'),
    path('energo_spravka', views.energo_spravka, name='energo_spravka'),
]
