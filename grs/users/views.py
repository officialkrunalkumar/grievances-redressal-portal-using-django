from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UpdateUserForm, UpdateProfileForm
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
    ''' Updating profile page and
    redinring the profile page'''
    if request.method == 'POST':
        p_form = UpdateProfileForm(
            request.POST,
            request.FILES,
            instance=request.user.profile)
        u_form = UpdateUserForm(request.POST, instance=request.user)
        if u_form.is_valid() and p_form.is_valid():
            p_form.save()
            u_form.save()
            messages.success(request, 'Your Account has been Update')
            return redirect('users:profile')
    else:
        p_form = UpdateProfileForm(instance=request.user.profile)
        u_form = UpdateUserForm(instance=request.user)
    complaints = Complaint.objects.all().filter(user=request.user).order_by('-id')
    print(complaints)
    context = {
        'p_form': p_form,
        'u_form': u_form,
        'complaints': complaints,
    }
    return render(request, 'users/profile.html', context)
