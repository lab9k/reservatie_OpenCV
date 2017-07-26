from django.conf.urls import url, include
from . import views

app_name = 'main'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'data/', views.data, name='data'),
    url(r'loading/', views.loading, name='loading')
]
