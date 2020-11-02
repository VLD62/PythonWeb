from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='index'),
    path('original/', views.original, name='original'),
]
