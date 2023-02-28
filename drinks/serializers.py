from dataclasses import field, fields
from pyexpat import model
from rest_framework import serializers
from .models import Drink

class Drinkserilizer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = ['id', 'name', 'description', 'short_description', 'price']

