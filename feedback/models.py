from django.db import models

class Feedback(models.Model):
    description = models.TextField()
    contact = models.EmailField(max_length=254)
    date = models.DateField()

    class Meta:
        ordering = ['-date']
