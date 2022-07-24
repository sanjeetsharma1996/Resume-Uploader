from wsgiref.validate import validator
from xml.dom import ValidationErr
from django import forms
from django.core.exceptions import ValidationError
from .models import ResumeModel

# def pin_number(value):
#     if value !=6:
#         raise ValidationErr("Enter six digite number ")


        
class ResumeForm(forms.ModelForm):
 class Meta:
  model = ResumeModel

  fields = ['name','email','dob', 'gender', 'locality', 'city', 'pin', 'mobile','state', 'job_city', 'profile_image', 'my_file']

  labels = {'name':'Full Name', 
            'email':'Email ID',
            'dob': 'Date of Birth',
            'gender':'Gemger',
            'pin':'Pin Code',
            'mobile':'Mobile No.',
            'job_city' :'Preferred Job Locations',
            'profile_image':'Profile Image',
            'my_file':'Document'
            }

  widgets = {
    'name':forms.TextInput(attrs={'class':'form-control'}),
    'email':forms.EmailInput(attrs={'class':'form-control'}),
    'dob':forms.DateInput(attrs={'class':'form-control', 'id':'datepicker'}),
    'gender':forms.RadioSelect(attrs={'class':'form-control'}),
    'locality':forms.TextInput(attrs={'class':'form-control'}),
    'city':forms.TextInput(attrs={'class':'form-control'}),
    'pin':forms.NumberInput(attrs={'class':'form-control'}),
    'mobile':forms.NumberInput(attrs={'class':'form-control'}),
    'state':forms.Select(attrs={'class':'form-select'}),
    'job_city':forms.CheckboxSelectMultiple(attrs={'class':'form-select'})
  }
  