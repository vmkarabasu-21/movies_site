from django.db import models
from django.contrib.auth .models import User
from django.db.models import Avg

class Movie(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    poster=models.ImageField(upload_to="posters/")
    year=models.IntegerField()
    language=models.CharField(max_length=50)
    category=models.CharField(max_length=50)
    trailer_url=models.URLField(blank=True,null=True)
    ott_name=models.CharField(max_length=50)
    ott_url=models.URLField(blank=True,null=True)

    
    def __str__(self):
        return self.title
    
    def average_rating(self):
        avg=self.rating_set.aggregate(Avg("stars"))["stars__avg"]
        return round(avg,1)if avg else 0


class Rating(models.Model):
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    stars=models.IntegerField()


class Review(models.Model):
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    comment=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}-{self.movie.title}"

class Watchlist(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE)

    def __str__(self):
        return self.movie.title    




    
