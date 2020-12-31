from django.forms import ModelForm, Textarea
from django.core.exceptions import ValidationError
from .models import std_registration_form, DisciplinaryIssue, CharacterCertificate
from django import forms

# Student Registration Form


class StdRegistration(forms.ModelForm):
    class Meta:
        model = std_registration_form
        fields = [
            'student_code',
            'name',
            'gender',
            'standard',
            'section',
            'Stream',
            'date_of_birth',
            'admission_no',
            'date_of_admission',
            'email',
            'CID',
            'class_teacher',
            'previous_school',
            'mobile_number',
            'permanent_address',
            'BoarderOrDayscholar',
            'RegularOrRepeater',
            'profile_pic',
            'father_name',
            'mother_name',
            'fathers_occupation',
            'mothers_occupation',
            'parents_mobile_number'
        ]
        widgets = {
            'student_code': forms.TextInput(attrs={'class': 'form-control',
                                                   'placeholder': 'Enter your Student Code'}),
            'name': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Enter your name'
                       }),
            'gender': forms.Select(
                attrs={'class': 'form-control'}),
            'standard': forms.Select(
                attrs={'class': 'form-control'}),
            'section': forms.Select(
                attrs={'class': 'form-control'}),
            'Stream': forms.Select(
                attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date'}),
            'admission_no': forms.NumberInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Enter your admission number'
                       }),
            'date_of_admission': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date',
                       'placeholder': 'Pick your admission date'
                       }),
            'email': forms.EmailInput(
                attrs={'class': 'form-control',
                       'placeholder': '.....@education.gov.bt'
                       }),
            'CID': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Enter CID number'
                       }),
            'class_teacher': forms.Select(
                attrs={'class': 'form-control'}),
            'previous_school': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Enter your previous school'
                       }),
            'mobile_number': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Enter 8 digit mobile number'
                       }),
            'permanent_address': forms.Textarea(
                attrs={'rows': 7, 'cols': 80, 'class': 'form-control',
                       'placeholder': 'Enter your permanent address: village, Gewog, Dzongkhag'
                       }),
            'BoarderOrDayscholar': forms.Select(
                attrs={'class': 'form-control'}),
            'RegularOrRepeater': forms.Select(
                attrs={'class': 'form-control'}),
            'profile_pic': forms.FileInput(
                attrs={'class': 'form-control'}),
            'father_name': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Your father name'
                       }),
            'mother_name': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Your mother name'
                       }),
            'father_name': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Your father name'
                       }),
            'fathers_occupation': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Enter father occupation'
                       }),
            'mothers_occupation': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Enter mother occupation'
                       }),
            'parents_mobile_number': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Enter 8 digit mobile number'
                       }),
        }

    def clean_student_code(self):
        std_code = self.cleaned_data.get('student_code')
        if std_code == "":
            raise forms.ValidationError("Required Field.")
        return std_code

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name == "":
            raise forms.ValidationError("Required Field.")
        return name

    def clean_CID(self):
        cid = self.cleaned_data.get('CID')
        if len(cid) != 11:
            raise forms.ValidationError(
                "CID number should be UNIQUE 11 digits.")
        return cid

    def clean_mobile_number(self):
        phone = self.cleaned_data.get('mobile_number')
        if len(phone) != 8:
            raise forms.ValidationError("Mobile number should have 8 digits.")
        return phone

    def clean_parents_mobile_number(self):
        phone = self.cleaned_data.get('parents_mobile_number')
        if len(phone) != 8:
            raise forms.ValidationError("Mobile number should have 8 digits.")
        return phone

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if "@education.gov.bt" not in email:
            raise forms.ValidationError(
                "We accept only education mail address(xyz@education.gov.bt).")
        return email

# Disciplinary issue Form


class DisciplinaryIssueform(forms.ModelForm):
    class Meta:
        model = DisciplinaryIssue
        fields = [
            'Student',
            'Violation_detail',
            'Violation_date',
            'Warning_decision',
            'Approved_by'
        ]
        widgets = {
            'Student': forms.Select(attrs={'class': 'form-control'}),
            'Violation_detail': forms.Textarea(
                attrs={'rows': 7, 'cols': 80, 'class': 'form-control',
                       'placeholder': 'Write about violation detail.'
                       }),
            'Violation_date': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date',
                       'placeholder': 'Pick violation date.'
                       }),
            'Warning_decision': forms.Textarea(
                attrs={'rows': 7, 'cols': 80, 'class': 'form-control',
                       'placeholder': 'Write about warning decision.'
                       }),
            'Approved_by': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Who approved warning decision?'
                       })
        }

# Character Certificate Form


class CharacterCertificateForm(forms.ModelForm):
    class Meta:
        model = CharacterCertificate
        fields = [
            'Student',
            'Category',
            'Description',
            'Awarded_on',
            'Awarded_by',
        ]
        widgets = {
            'Student': forms.Select(attrs={'class': 'form-control'}),
            'Category': forms.Select(attrs={'class': 'form-control'}),
            'Description': forms.Textarea(
                attrs={'rows': 7, 'cols': 80, 'class': 'form-control',
                       'placeholder': 'Brief description about the certificate.'
                       }),
            'Awarded_on': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date',
                       'placeholder': 'When was the certificate awarded?.'
                       }),

            'Awarded_by': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Who awarded the certificate?'
                       })
        }
