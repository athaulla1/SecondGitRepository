
from django.contrib import admin
from django.urls import path

from .views import *




#from music.views import * 

urlpatterns = [
    
    path("",index),   #music 
    path("add/", add),
    
]
