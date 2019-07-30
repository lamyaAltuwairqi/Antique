from django import forms
from django.contrib.auth.models import User
from .models import Profile, Items

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','email','password']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['mobile']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class ItemForm(forms.ModelForm):
    image = forms.ImageField(required=False)
    class Meta:
        model = Items
        fields = ['name', 'category', 'image', 'details', 'email', 'phone']
