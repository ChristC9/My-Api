from django.db import models

# Create your models here.


class ToDo(models.Model):

    title = models.TextField(max_length=250)
    body = models.TextField(max_length=250)

    def __str__(self):
        return self.title
