from django.db import models

# Create your models here.
class ToDo(models.Model):
    name=models.TextField(max_length=50)
    title=models.TextField(max_length=250)
    notes=models.TextField(max_length=500)
    pickup_location=models.TextField(max_length=50)
    dropoff_location=models.TextField(max_length=50)
    date=models.DateField()
    completed=models.BooleanField()
    
    def __str__(self):
        return self.name