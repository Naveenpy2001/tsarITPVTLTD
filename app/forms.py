from django import forms
from .models import UserRegistration

class ApplicantForm(forms.ModelForm):
    class Meta:
        model = UserRegistration
        fields = ['resume']