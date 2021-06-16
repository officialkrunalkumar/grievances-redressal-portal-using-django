from django.forms import fields
from .models import Complaint
from django import forms


class AddComplaintForm(forms.ModelForm):

    class Meta:
        model = Complaint
        fields = ['title', 'name', 'complaint_for', 'complaint_to', 'cohort', 'level', 'description', 'category']