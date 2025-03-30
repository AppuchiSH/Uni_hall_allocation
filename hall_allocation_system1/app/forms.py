"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _
from django import forms
from .models import CustomUser
from .models import HallRequest

class HallRequestForm(forms.ModelForm):
    class Meta:
        model = HallRequest
        fields = [
            'applicant', 'department', 'date', 'time', 'purpose',
            'podium', 'mic', 'led', 'stage', 'dias', 'participants'
        ]
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }


class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))
  

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'designation', 'phone_number', 'address']
        widgets = {
            'password': forms.PasswordInput()
        }

