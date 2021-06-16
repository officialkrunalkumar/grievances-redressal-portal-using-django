from django.shortcuts import render
from django.contrib import messages

# Create your views here.
from .models import Complaint
from .forms import AddComplaintForm


def add_complaint(request):
    form = AddComplaintForm(request.POST or None)
    if request.method == 'POST':
        form = AddComplaintForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            print(form)
            messages.success(request, 'Complaint Registered')
    return render(request, 'complaints/add_complaint.html', { 'form':form })