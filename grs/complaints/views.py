from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import Complaint
from .forms import AddComplaintForm


@login_required(login_url='login')
def add_complaint(request):
    form = AddComplaintForm(request.POST or None)
    if request.method == 'POST':
        form = AddComplaintForm(request.POST, instance=request.user)
        if form.is_valid():
            complaint = Complaint(
                title=request.POST['title'],
                name=request.POST['name'],
                complaint_for=request.POST['complaint_for'],
                complaint_to=request.POST['complaint_to'],
                cohort=request.POST['cohort'],
                level=request.POST['level'],
                description=request.POST['description'],
                category=request.POST['category'],
                user=request.user
            )
            complaint.save()
            messages.success(request, 'Complaint Registered')
    return render(request, 'complaints/add_complaint.html', { 'form':form }) 