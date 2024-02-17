from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
#from .forms import SignUpForm, AddRecordForm
from django.contrib.auth.decorators import login_required
#from .models import Record


def index(request):
    return render(request, 'index.html')