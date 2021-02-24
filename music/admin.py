from django.contrib import admin
from .models import *
# Register your models here.

class AlbumAdmin(admin.ModelAdmin):
    list_display=['album_id','album_name','album_pic','musdir']

admin.site.register(Album,AlbumAdmin)

class SongAdmin(admin.ModelAdmin):
    list_display=['sname','singer','album_id']

admin.site.register(Song,SongAdmin)
