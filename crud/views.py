from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from django.contrib.auth.decorators import login_required
from .models import Record


def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have Successfully Register!")
            return redirect('home')
        
    else:
        form = SignUpForm()
        return render(request, 'signup.html', {'form':form})

    return render(request, 'signup.html', {'form':form})


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been Logged in!")
            return redirect('home')
        else:
            messages.success(request,"There was an Error!")
            return redirect('signin')
        
    else:
        return render(request, 'signin.html')
    
@login_required(login_url='signin')
def home(request):
    return render(request, 'home.html')

@login_required(login_url='signin')
def signout(request):
    logout(request)
    messages.success(request, "You have been Logged Out Successfully!")
    return redirect('index')

@login_required(login_url='signin')
def report(request):
	records = Record.objects.all()
	return render(request, 'report.html', {'records':records})
