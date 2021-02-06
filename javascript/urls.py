from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'javascript'


urlpatterns = [
    
    path('console', views.console, name='console'),
    path('events', views.events, name='events'),
    path('traverse', views.traverse, name='traverse'),
    
]
