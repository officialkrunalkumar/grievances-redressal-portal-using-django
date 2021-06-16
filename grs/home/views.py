from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
from complaints.models import Complaint


@login_required(login_url='login')
def home(request):
    complaints = Complaint.objects.all().filter(user = request.user)
    print(complaints)
    context = {
        'complaints':complaints
    }
    return render(request, 'home/home.html',context)
