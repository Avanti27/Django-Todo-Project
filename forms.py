from django import forms
from .models import Course,Student
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

'''
class StudentRegistrationForm(forms.Form):

    name=forms.CharField()
    email=forms.EmailField()


'''
class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model=Student
        #fields=['name','email']
        exclude=['name']

class SignUpForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']        