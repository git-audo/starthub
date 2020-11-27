from django.db import models
from django.contrib.postgres.fields import ArrayField
from datetime import date


class Post(models.Model):
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=120)
    detailed_description = models.TextField()
    author = models.CharField(max_length=200)
    publication_date = models.DateField()
    email = models.EmailField(max_length=254)
    tags =  ArrayField(
            models.CharField(max_length=50, blank=True),
            size=3,
            null=True,
            blank=True
        )

    @property
    def is_today(self):
        return date.today() <= self.publication_date

    def is_yesterday(self):
        return (date.today()-self.publication_date).days == 1
    
    class Meta:
        ordering = ['-publication_date']
    
    def __str__(self):
        return self.title
