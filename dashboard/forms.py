from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password')
        widgets = {

            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),

            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),

            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),

            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),

            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),

        }
    def clean_password(self):
        # Hash the password before saving it to the database
        password = self.cleaned_data['password']
        hashed_password = make_password(password)
        return hashed_password     
 
