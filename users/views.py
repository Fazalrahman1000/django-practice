from django.shortcuts import render, redirect
from .forms import RegisterUser
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def create_user(request):
    if request.method == 'POST':
        form = RegisterUser(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            message = messages.success(request, f"Welcome {username} to our website, your account is created")
            return redirect('user:login')
    else:
        form = RegisterUser()
    return render(request, 'users/create_user.html', {'form':form})

@login_required
def profilepage(request):

    return render(request, 'users/profile.html')