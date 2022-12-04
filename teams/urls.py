from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.teams, name='teams'),
    path('fixtures', views.fixtures, name='fixtures'),
    path('table', views.table, name='table'),
    path('create', views.create, name='create'),
    path('register_fixture', views.register_fixture, name = 'register_fixture'),
]
urlpatterns +=  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns+=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)