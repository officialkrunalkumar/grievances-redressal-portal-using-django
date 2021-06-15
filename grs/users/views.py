from django.shortcuts import render
from django.contrib import messages
from .forms import UserRegisterForm
# Create your views here.


def register(request):
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, f"Congratulation! You are registed with MountBlue's GRS.")
    return render(request, 'users/register.html', {'form': form})
