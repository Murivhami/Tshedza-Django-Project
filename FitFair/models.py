from django.contrib.auth.models import AbstractUser
from django.db import models
import datetime
from django.db.models import Sum

#model for user details.
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

#Model for storing the meal details.
class Meal(models.Model):
    user= models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    MEALTYPE_CHOICES = [
    ('breakfast', 'breakfast'),
    ('lunch', 'lunch'),
    ('dinner', 'dinner')
    ]
    meal_of_the_day = models.CharField(max_length=255,choices=MEALTYPE_CHOICES, null=True, blank=True)
    food_item = models.CharField(max_length=255, null=True, blank=True)
    fats = models.CharField(max_length=255, null=True, blank=True)
    proteins = models.CharField(max_length=255, null=True, blank=True)
    carbs = models.CharField(max_length=255, null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    total_calories = models.PositiveIntegerField(null = True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.meal_of_the_day} - {self.total_calories} kcal"


#According to nutritional principles, carbs, and proteins contribute 4 calories per gram. 
# Fats contribute 9 calories per gram, Fiber 2 calories per gram.
    

    #def __str__(self):
        #return f"{self.user} - {self.mealtype} - {self.total_calories} intake on {self.date}"
     
#Model for storing the nutritional product details.


