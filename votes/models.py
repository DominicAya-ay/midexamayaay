from django.db import models

# Create your models here.

class Position(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name

class Candidate(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    birthdate = models.DateTimeField("Birthdate")
    platform = models.TextField()

    def __str__(self):
        return self.lastname + ", " + self.firstname

class Vote(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    vote_datetime = models.DateTimeField("Date Voted", auto_now_add=True)

    def __str__(self):
        return self.vote_datetime
