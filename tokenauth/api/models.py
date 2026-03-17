from django.db import models

# Create your models here.

class fresh(models.Model):
    title=models.CharField(max_length=200)
    Content=models.TextField()

    def __str__(self):
        return self.title