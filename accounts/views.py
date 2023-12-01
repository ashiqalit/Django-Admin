from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

# Create your views here.
def register(request):
    if 'username' in request.session:
        return redirect('/')
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        # hashed_password = make_password(password2)
        

        if password1 == password2:
            if User.objects.filter(username = username).exists():
                messages.info(request, 'Username already taken')
                return redirect('register')
            elif User.objects.filter(email = email).exists():
                messages.info(request, 'Email already taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password2, email=email, first_name=first_name, last_name=last_name)
                user.save();    
                print('user created')
                return redirect('login')
        else:
            messages.info(request, 'Password not matching')     
            return redirect('register')
        return redirect('/')
        
    else:
        return render(request, 'register.html')

def login(request):
    if 'username' in request.session:
        return redirect ('/')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None :  
            auth.login(request, user)
            request.session['username'] = username
            return redirect('/')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')

    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')