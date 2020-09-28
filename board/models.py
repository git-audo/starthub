from django.db import models
from django.contrib.postgres.fields import ArrayField

class Post(models.Model):
    PHASES = [
        ('I', 'Ideazione'),
        ('S', 'Sviluppo'), 
        ('D', 'Distribuzione'),        
    ]
    
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=120)
    author = models.CharField(max_length=200)
    publication_date = models.DateField()
    tag =  ArrayField(
            models.CharField(max_length=50, blank=True),
            size=3,
            null=True,
            blank=True
        )
    phase = models.CharField(
        max_length=1,
        choices=PHASES,
    )

    class Meta:
        ordering = ['-publication_date']
    
    def __str__(self):
        return self.title
