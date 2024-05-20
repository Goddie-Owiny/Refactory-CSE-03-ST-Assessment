
from django import forms
from django.forms import Form
from .models import *


#models here

class regform(forms.ModelForm):
    class Meta:
        model = Reg
        fields = ['fname', 'lname', 'course', 'entryscheme', 'intake', 'sponsorship', 'gender', 'dob', 'residence']

    def clean_date_of_birth(self):
        dob = self.cleaned_data['date of birth']
        if dob == timezone.now().date():
            raise ValidationError("Date of birth should be in the past.")
        if dob >= timezone.now().date():
            raise ValidationError("Date of birth should not be in the future.")
        age = timezone.now().date().year - dob.year - ((timezone.now().date().month, timezone.now().date().day) < (dob.month, dob.day))
        if age < 18:
            raise ValidationError("You must be at least 18 years old to register.")
        return dob