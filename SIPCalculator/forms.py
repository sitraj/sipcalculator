from django import forms
from .models import SIPCalculator

class SIPCalculatorForm(forms.ModelForm):
    class Meta:
        model = SIPCalculator
        fields = ['initial_investment', 'monthly_investment', 'annual_rate', 'time_period']
