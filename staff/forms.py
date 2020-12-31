from django.forms import *
from django.core.exceptions import ValidationError
from .models import StaffDetail
from django import forms
from students.validators import *


class StaffRegistrationForm(forms.ModelForm):
    class Meta:
        model = StaffDetail
        fields = [
            'Employee_ID', 'name', 'gender', 'date_of_birth', 'CID',
            'category', 'position_title', 'position_level', 'grade', 'appointment_date',
            'joining_date_of_present_school', 'transfered_from', 'Employment_type',
            'nationality', 'subject', 'qualification', 'contact_number', 'email',
            'permanent_address', 'profile_pic'
        ]
        widgets = {
            'Employee_ID': forms.NumberInput(attrs={'class': 'form-control',
                                                    'placeholder': 'Enter your Employee Id'}),
            'name': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Enter your name'
                       }),
            'gender': forms.Select(
                attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date'}),
            'CID': forms.NumberInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Enter CID number'
                       }),
            'category': forms.Select(
                attrs={'class': 'form-control'}),
            'position_title': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Enter Position Title'
                       }),
            'position_level': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Enter your position level'}),
            'grade': forms.NumberInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Enter your grade in number'}),
            'appointment_date': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date',
                       'placeholder': 'Pick your appointment date'
                       }),
            'joining_date_of_present_school': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date',
                       'placeholder': 'When did you joined to this school?'
                       }),
            'transfered_from': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Your previous school'
                       }),
            'Employment_type': forms.Select(
                attrs={'class': 'form-control'}),
            'nationality': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Enter your nationality'
                       }),
            'subject': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Enter your elective subject'
                       }),
            'qualification': forms.Textarea(
                attrs={'rows': 7, 'cols': 80, 'class': 'form-control',
                       'placeholder': 'Enter all your qualification'
                       }),
            'contact_number': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Enter 8 digit mobile number'
                       }),
            'email': forms.EmailInput(
                attrs={'class': 'form-control',
                       'placeholder': '.....@education.gov.bt'
                       }),
            'permanent_address': forms.Textarea(
                attrs={'rows': 7, 'cols': 80, 'class': 'form-control',
                       'placeholder': 'Enter your permanent address: village, Gewog, Dzongkhag'
                       }),
            'profile_pic': forms.FileInput(
                attrs={'class': 'form-control'})
        }

    def clean_CID(self):
        cid = self.cleaned_data.get('CID')
        if len(cid) != 11:
            raise forms.ValidationError(
                "CID number should be UNIQUE 11 digits.")
        return cid

    def clean_contact_number(self):
        phone = self.cleaned_data.get('contact_number')
        if len(phone) != 8:
            raise forms.ValidationError("Mobile number should have 8 digits.")
        return phone

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if "@education.gov.bt" not in email:
            raise forms.ValidationError(
                "We accept only education mail address.")
        return email
