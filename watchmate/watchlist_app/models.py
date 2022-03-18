from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class StreamPlatform(models.Model):
    name = models.CharField(max_length=30)
    about = models.CharField(max_length=150)
    website = models.URLField(max_length=100)

    def __str__(self):
        return self.name


class WatchList(models.Model):

    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    platform = models.ForeignKey(
        StreamPlatform, on_delete=models.CASCADE, related_name="watchedlist")
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    review_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="review_user")
    rating = models.IntegerField()
    description = models.CharField(max_length=50)
    active = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    watchlist = models.ForeignKey(
        WatchList, on_delete=models.CASCADE, related_name="review")

    def __str__(self):
        return str(self.rating) + " | "+self.description
