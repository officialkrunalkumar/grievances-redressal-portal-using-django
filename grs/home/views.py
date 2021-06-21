from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from complaints.models import Complaint
# Create your views here.


def home(request):
    return render(request, 'home/home.html')
