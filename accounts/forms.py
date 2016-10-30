from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']




class ExtendedUserCreationForm(UserCreationForm): 
    first_name = forms.CharField(max_length=150, required=True)
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 
                   "first_name")