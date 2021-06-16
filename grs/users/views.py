from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
# Create your views here.
from complaints.models import Complaint


def register(request):
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Congratulation! \
                         You are registed with MountBlue's GRS.")
    return render(request, 'users/register.html', {'form': form})


@login_required(login_url='login')
def profile(request):
    complaints = Complaint.objects.all().filter(user=request.user)
    print(complaints)
    context = {
        'complaints': complaints
    }
    return render(request, 'users/profile.html', context)
