from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    position = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
      return "Name: {}, Contact: {}".format(self.name, self.position)
    class Meta:
        db_table = 'employee'



    

    
