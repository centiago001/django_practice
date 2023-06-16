from django.db import models

class Enquery(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    massage=models.CharField(max_length=500)


def __str__(self):
        return self.name

# Create your models here.
