from tkinter import TRUE
from django.db import models

class Drink(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    short_description = models.CharField(max_length=500, null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)

    def __str__(self):
        return self.name + ', ' + self.description

