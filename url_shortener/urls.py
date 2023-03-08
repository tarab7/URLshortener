from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('hello', views.hello_world),
    path('task', views.task),
    path('', views.home_page),
    path('analytics', views.analytics),
    path('<slug:custom_name>', views.redirect_url),
]
#slugs contain character, digits, symbol