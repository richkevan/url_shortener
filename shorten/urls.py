from django.urls import path
from . import views

urlpatterns = [
    path('<str:short_url>', views.redirect, name='redirect'),
    path('', views.IndexView, name='index'),
]