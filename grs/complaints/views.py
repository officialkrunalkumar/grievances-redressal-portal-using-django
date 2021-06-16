from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied 
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


@login_required(login_url='login')
def delete_complaint(request, id):
    complaint = get_object_or_404(Complaint, id=id)
    if request.user == complaint.user:
        complaint.delete()
        messages.success(request, "Deleted Succesfully!")
        return redirect('users:profile')
    else:
        raise PermissionDenied("You Don't Have Persmission to do that") 


@login_required(login_url='login')
def update_complaint(request, id):
    complaint = get_object_or_404(Complaint, id=id)
    if request.user == complaint.user:
        if request.method == 'POST':
            form = AddComplaintForm(request.POST, instance=request.user)
            if form.is_valid():
                complaint = Complaint(
                                id = complaint.id,
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
        else:
            form = AddComplaintForm(instance = complaint)
        return render(request, 'complaints/add_complaint.html', {'form': form})
    else:
        raise PermissionDenied("You Don't Have Persmission to do that") 