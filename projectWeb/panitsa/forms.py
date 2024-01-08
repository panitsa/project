from django import forms
from django.contrib.auth.forms import *
from .models import *

class AdminLoginForm(forms.Form):
    username = forms.CharField(label='ชื่อผู้ใช้', max_length=100)
    password = forms.CharField(label='รหัสผ่าน', widget=forms.PasswordInput)

class RepresentativeForm(forms.ModelForm):
    class Meta:
        model = Representative
        fields = ['image', 'first_name', 'last_name', 'position', 'phone_number']

class Activity_newsForm(forms.ModelForm):
    class Meta:
        model = Activity_news
        fields = ['text', 'date', 'time', 'image', 'image1']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
            'image': forms.ClearableFileInput(),
            'image1': forms.ClearableFileInput(),
        }
    
class VillagepublicForm(forms.ModelForm):
    class Meta:
        model = Villagepublic
        fields = ['image', 'first_name', 'last_name', 'position', 'phone_number']
