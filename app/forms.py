from django import forms


# class JobApplicationForm(forms.ModelForm):
#     class Meta:
#         model = JobApplication
#         fields = ['name', 'email', 'resume', 'is_fresher']

from .models import MediaPost

class MediaPostForm(forms.ModelForm):
    class Meta:
        model = MediaPost
        fields = '__all__'