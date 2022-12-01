from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('fixtures', views.fixtures, name='fixtures'),
    path('table', views.table, name='table'),
    path('update', views.update, name='update'),
]