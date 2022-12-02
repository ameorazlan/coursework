from django.urls import path
from . import views

urlpatterns = [
    path('', views.teams, name='teams'),
    path('fixtures', views.fixtures, name='fixtures'),
    path('table', views.table, name='table'),
    path('create', views.create, name='create'),
]