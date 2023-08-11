"""p123 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from . import views,search1,search2
from TestModel import testdb
from django.conf.urls import url

urlpatterns = [
    path('',views.hello),
    path('admin/', admin.site.urls),
    path('abc/',views.hello),
    path('r1/',views.r1),
    path('r2/', views.r2),
    path('r3/', views.r3),
    path('testdb/',testdb.testdb),
    path('getform/',search1.search_form),
    path('search1/',search1.search),
    path(r'postform/',search2.search_post),
    path('testrequest/',views.req)
]
