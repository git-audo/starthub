from django.db import models

class Venture(models.Model):
    PHASES = [
        ('I', 'Ideazione'),
        ('S', 'Sviluppo'), 
        ('D', 'Distribuzione'),        
    ]
    
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publication_date = models.DateField()
    tag = models.CharField(max_length=100)
    phase = models.CharField(
        max_length=1,
        choices=PHASES,
    )
    
    def __str__(self):
        return self.title
