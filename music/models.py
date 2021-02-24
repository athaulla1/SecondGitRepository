from django.db import models

# Create your models here.

class Album(models.Model):
    album_id = models.IntegerField(primary_key=True)
    album_name = models.CharField(max_length=100)
    album_pic  = models.CharField(max_length=250)
    musdir = models.CharField(max_length=100)

    def __str__(self):
        return self.album_name

class Song(models.Model):
    sname = models.CharField(max_length=70)
    singer = models.CharField(max_length=150)
    album_id = models.ForeignKey(Album,on_delete=models.CASCADE)



# C --
# R --
# U ---
# D---