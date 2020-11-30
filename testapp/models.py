from django.db import models

# Create your models here.


class MovieModel(models.Model):
    r_date = models.DateField()
    movie_name = models.CharField(max_length=64)
    hero = models.CharField(max_length=64)
    heroine = models.CharField(max_length=64)
    rating = models.IntegerField()
