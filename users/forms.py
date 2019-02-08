from django import forms
from .models import *
from django.contrib.auth import authenticate,get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.db import models


class UserForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email','first_name','last_name', 'password1', 'password2']

        

class ProfileForm(forms.ModelForm):
  
    class Meta:
        model = Profile
        fields = ['phone', 'profile_img']
class signup(forms.Form):
    username = forms.CharField(label="username")
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"enter your password"})) 
    def clean(self,*args,**kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            user=authenticate(username = username ,password = password)
            if not user:
                raise forms.ValidationError('the user not exists')
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect password')
            if not user.is_active:
                raise forms.ValidationError('This user is not active')
        return super(signup,self).clean(*args,**kwargs)
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields =['first_name','last_name']
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone','country','facebook','profile_img']

          
        