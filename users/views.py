from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.

def create_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            message = messages.success(request, f"Welcome {username} to our website, your account is created")
            return redirect('foods:index')
    else:
        form = UserCreationForm()
    return render(request, 'users/create_user.html', {'form':form})