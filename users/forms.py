from django import forms
from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from . models import CustomUser


class CustomUserCreationForm(UserCreationForm):


    class Meta:
        model = CustomUser
        fields = ('email',)


class CustomUserChnageForm(UserChangeForm):


    class Meta:
        model = CustomUser
        fields = ('email',)


class UserRegistrationForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))



class UserLoginForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    


class ProfileImageForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ('image',)
