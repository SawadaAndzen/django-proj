from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=200)
    genres = models.ManyToManyField(Genre)
    release_year = models.PositiveIntegerField()
    rating = models.FloatField()

    def __str__(self):
        
        return self.title