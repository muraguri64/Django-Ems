from django.shortcuts import render,redirect
from django.http import HttpResponse

# for authentication
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.

def signup(request):
    if request.method == 'GET':
        return render(request, 'accounts/signup.html')
    elif request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error':'Username exists bro!'})
            except User.DoesNotExist:
                user = User.objects.create_user(username = request.POST['username'], password=request.POST['password1'], email = request.POST['email'], is_active=False)
                auth.login(request,user)
                return redirect('polls_index')



def login(request):

    if request.method == 'GET':
        return render(request, 'accounts/login.html')
    elif request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('polls_index')
        else:
            return render(request, 'accounts/login.html',{'error':'Error in credentials!'})

def logout(request):

    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
