from django.conf.urls import url
from . import views
'''
Created on 1 jul. 2017

@author: Figueroa8a
'''

urlpatterns = [
    url(r'', views.post_list, name="lista_slider"),
]