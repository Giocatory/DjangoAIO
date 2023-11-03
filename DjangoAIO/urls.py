"""
URL configuration for DjangoAIO project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

import for_eko
import for_energo
import for_fkr
from jku import for_ikibzyak

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls'), name='main'),
    path('fkr/', include('fkr.urls'), name='fkr'),
    path('eko/', include('eko.urls'), name='eko'),
    path('energo/', include('energo.urls'), name='energo'),
    path('ikibzyak/', include('ikibzyak.urls'), name='ikibzyak'),
]


for_fkr.fkr_connect_db()
for_eko.eko_connect_db()
for_energo.energo_connect_db()
for_ikibzyak.ikibzyak_connect_db()
