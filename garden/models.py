from django.db import models
from accounts.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.

class Garden(models.Model):
    TYPE_CHOICES = [
    ('ALLOT', 'Allotment'),
    ('GARDEN', 'Garden')
    ]
    owner = models.ForeignKey(User, on_delete=models.PROTECT, blank=True)
    name = models.CharField(max_length=100)
    width = models.PositiveIntegerField(validators=[MaxValueValidator(30, "width cannot exceed 30 meters")])
    length = models.PositiveIntegerField(validators=[MaxValueValidator(30, "length cannot exceed 30 meters")])
    type = models.CharField(choices=TYPE_CHOICES, max_length=6, default='GARDEN')

class GardenStructure(models.Model):
    TYPE_CHOICES = [
    ('BUILD', 'Building'),
    ('WATER', 'Water Feature'),
    ('CONT', 'Container'),
    ('PATH', 'Path')
    ]
    topLeftx = models.PositiveIntegerField()
    topLefty = models.PositiveIntegerField()
    width = models.PositiveIntegerField()
    height = models.PositiveIntegerField()
    type = models.CharField(choices=TYPE_CHOICES, max_length=5, default='Build')
    garden = models.ForeignKey(Garden, on_delete=models.CASCADE, blank=True, null=True)
