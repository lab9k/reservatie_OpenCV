from django.conf.urls import url, include
from . import views

app_name = 'main'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'data/', views.data, name='data'),
    url(r'loading/', views.loading, name='loading'),
    url(r'confirmation/', views.confirmation, name='confirmation'),
    url(r'error/', views.error, name='error'),
    url(r'camera/', views.camerafunction, name='camera'),
    url(r'facerec/', views.facerec,name='facerec'),
    url(r'noRoom/', views.noRoom, name='noRoom'),
    url(r'noPerson/', views.noPerson, name='noPerson')
]
