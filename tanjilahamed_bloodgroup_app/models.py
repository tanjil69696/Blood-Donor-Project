from django.db import models

# Create your models here.
class blooddonation(models.Model):
    name = models.CharField(max_length=100)
    number = models.IntegerField()
    address = models.TextField(max_length=100)
    bloodgroup = models.TextField(max_length=3)
    donationdate = models.DateField()

    def __str__(self):
        return self.name