from django.db import models

class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, default='')

class Rating(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    movie_id = models.IntegerField()
    user_id = models.IntegerField()
    rating = models.IntegerField(choices=RATING_CHOICES)