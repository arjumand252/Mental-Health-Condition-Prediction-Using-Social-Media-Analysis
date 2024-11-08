from django import forms
from .models import Survey

class SurveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = '__all__'
        widgets = {
            'datetime': forms.DateTimeInput(attrs={'readonly': 'readonly'}),
            # Customize widgets as needed
        }
        