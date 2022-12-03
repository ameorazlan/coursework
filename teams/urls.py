from django.urls import path
from . import views

urlpatterns = [
    path('', views.teams, name='teams'),
    path('fixtures', views.fixtures, name='fixtures'),
    path('table', views.table, name='table'),
    path('create', views.create, name='create'),
    path('register_fixture', views.register_fixture, name = 'register_fixture'),
]