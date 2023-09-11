from django.urls import path

import for_eko
import for_fkr
from . import views


urlpatterns = [
    path('', views.eko, name='eko'),
]

for_fkr.fkr_connect_db()
for_eko.eko_connect_db()
