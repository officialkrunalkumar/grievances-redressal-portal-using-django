from .models import Complaint, Feedback
from django import forms


class AddComplaintForm(forms.ModelForm):

    class Meta:
        model = Complaint
        fields = ['title', 'name', 'complaint_for', 'complaint_to',
                  'cohort', 'level', 'description', 'category']


class AddFeedbackForm(forms.ModelForm):

    class Meta:
        model = Feedback
        fields = ['rating', 'description']
