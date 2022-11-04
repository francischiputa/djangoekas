from django import forms
from .models import LoanApplication


class LoanApplicationForm(forms.ModelForm):
    class Meta:
        model = LoanApplication
        fields = '__all__'
        exclude = [
            'confirmed', 'date_time_created', ''
        ]