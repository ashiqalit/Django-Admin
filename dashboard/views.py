from django.shortcuts import render, redirect
from django.contrib import messages, admin
from django.contrib.auth.models import User, Group  
from django.contrib import auth
from .forms import UserForm
from .filters import UserFilter
# Create your views here.



def login(request):
    if 'username' in request.session:
        
        return redirect('dash')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user_ = auth.authenticate(username=username, password=password)
            
        if user_ is not None:
            if not user_.is_superuser:
                messages.info(request, 'You do not have admin privilegs')
                return redirect('dashboard_login')
            auth.login(request, user_)
            request.session['username'] = username
            return redirect('dash')       
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('dashboard_login')
    else:
        return render(request, 'admin_login.html')

def logout(request):
    if 'username' in request.session:
        request.session.flush()
    auth.logout(request)
    return redirect('dash')

def dash(request):
    if not 'username' in request.session:
        return redirect('dashboard_login')
    return render(request, 'dashboard.html')
    

def create_user(request):  
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('read_user')
        else:
            messages.info(request, 'Form invalid')
            return redirect('create_user')
    else:
        form = UserForm()
        return render(request, 'create.html', {'form':form})

def read_user(request):
    users = User.objects.all()
    myFilter = UserFilter(request.GET, queryset=users)
    filterd_users = myFilter.qs
    context = {'all_users' : filterd_users, 'myFilter' : myFilter}
    return render(request, 'read.html', context)

def update_user(request, pk):
    user = User.objects.get(id=pk)
    form = UserForm(instance=user)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('read_user')
    else:
        context = {
            'user' : user,
            'form' : form,
        }    
        return render(request, 'update.html', context)

def delete_user(request, pk):
    user = User.objects.get(id=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('read_user')
    return render(request, 'delete.html', {'user':user})