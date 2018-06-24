from django.db import models
from django.urls import reverse

class Album(models.Model):
    artist = models.CharField(max_length=100)
    album_title = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    album_logo = models.FileField()

    def get_absolute_url(self):
        return reverse('music_ns:detail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.album_title + ' --by-- ' + self.artist


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)
    is_fav= models.BooleanField(default=False)

    def __str__(self):
        return self.song_title + '.' + self.file_type