from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator



class MyWatchListModel(models.Model):
    watched = models.BooleanField()
    title = models.CharField(max_length=255)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    release_date = models.CharField(max_length=255)
    review = models.TextField()
