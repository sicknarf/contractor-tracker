from django.forms import ModelForm
from django import forms
from .models import Task
from django.contrib.auth.forms import UserCreationForm 
from django.forms.fields import EmailField  
from django.contrib.auth.models import User  
from django.core.exceptions import ValidationError



class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['description']

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(label='username', min_length=5, max_length=150)
    email = forms.EmailField(label='email')
    first_name = forms.CharField(label='first name', min_length=2, max_length=30)
    last_name = forms.CharField(label='first name', min_length=2, max_length=30)
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)
    license_number = forms.CharField(label='License Number', widget=forms.NumberInput)

    def username_clean(self):  
        username = self.cleaned_data['username'].lower()  
        new = User.objects.filter(username = username)  
        if new.count():  
            raise ValidationError("User Already Exist")  
        return username  
  
    def email_clean(self):  
        email = self.cleaned_data['email'].lower()  
        new = User.objects.filter(email=email)  
        if new.count():  
            raise ValidationError(" Email Already Exists")  
        return email  

    def license_clean(self):
        license_number = self.cleaned_data['license_number'].lower()
        new = User.objects.filter(license_number=license_number)
        if new.count():
            raise ValidationError("License number already in use, please contact admin")
        return license_number
  
    def clean_password2(self):  
        password1 = self.cleaned_data['password1']  
        password2 = self.cleaned_data['password2']  
  
        if password1 and password2 and password1 != password2:  
            raise ValidationError("Passwords don't match")  
        return password2  
  
    def save(self, commit = True):  
        user = User.objects.create_user(  
            self.cleaned_data['username'],  
            self.cleaned_data['email'],  
            self.cleaned_data['password1']  
        )  
        return user  