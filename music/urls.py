from django.contrib import admin
from django.urls import path, re_path

app_name="music"


from music.views import * 


#from music.views import * 

urlpatterns = [
    path('', index,name="musichome"),
    path('homelist/',indexlist),


    #http://localhost:8000/music/search/1001
    #1001, 1002,1003,1004.............
    #path('search'/<int:albumid>, search)
    #RE 
    path('delete/',delete),
    re_path(r'^search/([0-9,A-Z,a-z]+)/$', search)
    #r'^(?P<album_id>[0-9]+)/$'
#?P<albumid>
]