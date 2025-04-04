from django.test import TestCase
from .models import Meal
from django.contrib.auth import get_user_model
from datetime import date

#Testcase for Meal model
class MealModelTestCase(TestCase):
    def setUp(self):
        #Creating a user as this is the first step when logging into the app.
        self.user = get_user_model().objects.create_user(
            username='testuser', 
            email='testuser@example.com',
            password='testpassword'
        )

    #Logic for testing of logging the meal

    def test_create_meal(self):
        meal = Meal.objects.create(
            user = self.user,
            meal_of_the_day = 'lunch',
            food_item = 'apple',
            fats = 10,
            proteins = 30,
            carbs = 45,
            quantity = 2,
            total_calories = 125,
            date = date(2025, 4, 2)
        )

        self.assertEqual(meal.meal_of_the_day, 'lunch')
        self.assertEqual(meal.food_item, 'apple')
        self.assertEqual(meal.fats, 10)
        self.assertEqual(meal.proteins, 30)
        self.assertEqual(meal.carbs, 45)
        self.assertEqual(meal.quantity, 2)
        self.assertEqual(meal.total_calories, 125)
        self.assertEqual(meal.date, date(2025, 4, 2))
        self.assertEqual(meal.user.username, 'testuser')

#Test for registering a user
CustomUser = get_user_model()

class CustomUserModelTest(TestCase):

    def setUp(self):
        """Set up test data."""
        self.user = CustomUser.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="password123",
            age=25,
            location="JHB"
        )
    def test_user_creation(self):
        """Test that a user is created successfully."""
        self.assertEqual(self.user.username, "testuser")
        self.assertEqual(self.user.email, "test@example.com")
        self.assertEqual(self.user.age, 25)
        self.assertEqual(self.user.location, "JHB")
        self.assertTrue(self.user.check_password("password123"))

    def test_location_choices(self):
        """Test that location choices are valid."""
        valid_locations = dict(CustomUser.CITY_CHOICES).keys()
        self.assertIn(self.user.location, valid_locations)

    def test_default_location_is_null(self):
        """Test that location defaults to null if not provided."""
        user_without_location = CustomUser.objects.create_user(
            username="user2", email="user2@example.com", password="password123", age=30
        )
        self.assertIsNone(user_without_location.location)
    
    def test_age_optional(self):
        """Test that age can be null."""
        user_without_age = CustomUser.objects.create_user(
            username="user3", email="user3@example.com", password="password123", location="CPT"
        )
        self.assertIsNone(user_without_age.age)

    def test_string_representation(self):
        """Test the __str__ method of the user."""
        self.assertEqual(str(self.user), "testuser")

    def test_is_major(self):
        """Test custom methods, like checking if the user is an adult."""
        self.assertTrue(self.user.age >= 18)

    def test_invalid_age(self):
        """Test invalid age values."""
        with self.assertRaises(ValueError):
            CustomUser.objects.create_user(
                username="user4",
                email="user4@example.com",
                password="password123",
                age=-5,  # Invalid age
                location="JHB"
            )





    
    