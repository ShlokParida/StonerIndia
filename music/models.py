from django.db import models

class Music(models.Model):
    track_name = models.CharField(max_length = 100)
    track_link = models.URLField()
    track_thumbnail=models.ImageField(upload_to = 'media/images/Music')
    # track_file = models.FileField(upload_to = 'media/tracks')
    def __str__(self):
        return self.track_name
