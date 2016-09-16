from django.db import models


class Movie(models.Model):
    movie_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)

    def __unicode__(self):
        return self.title
