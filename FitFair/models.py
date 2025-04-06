from django.contrib.auth.models import AbstractUser
from django.db import models
import datetime

#Model for storing user details.
class CustomUser(AbstractUser):
    CITY_CHOICES = [
        ('JHB', 'Johannesburg'),
        ('CPT', 'Cape Town'),
        ('DBN', 'Durban'),
        ('PTA', 'Pretoria'),
        ('BFN', 'Bloemfontein'),
        ('PLZ', 'Port Elizabeth'),
        ('EL', 'East London'),
        ('PLK', 'Polokwane'),
        ('NLP', 'Nelspruit'),
        ('KIM', 'Kimberley'),
        ('RST', 'Rustenburg'),
        ('PMB', 'Pietermaritzburg')
    ]
    age = models.PositiveIntegerField(null=True, blank=True)
    location = models.CharField(max_length=255, choices=CITY_CHOICES, null=True, blank=False)
    

    def __str__(self):
        return self.username

#Model for storing the meal details for a user.
class Meal(models.Model):
    user= models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    MEALTYPE_CHOICES = [
    ('breakfast', 'breakfast'),
    ('lunch', 'lunch'),
    ('dinner', 'dinner'),
    ('snack', 'snack')
    ]
    meal_of_the_day = models.CharField(max_length=255,choices=MEALTYPE_CHOICES, null=True, blank=True)
    food_item = models.CharField(max_length=255, null=True, blank=True)
    fats = models.FloatField(null=True)
    proteins = models.FloatField(null=True)
    carbs = models.FloatField(null = True)
    quantity = models.IntegerField(null=True, blank=True)
    total_calories = models.FloatField(null=True)
    date = models.DateField()

    def __str__(self):
        return f"{self.meal_of_the_day} - {self.total_calories} kcal"



