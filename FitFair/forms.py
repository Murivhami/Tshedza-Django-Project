from django import forms
from FitFair.models import Meal

class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = '__all__'
        widgets = {'meal_type': forms.Select(attrs={'class': 'form-control'}),  # Dropdown populated from MealType
            'food_item': forms.Select(attrs={'class': 'form-control'}),
            'total_calories': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter quantity'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Optional notes'}),
        }

