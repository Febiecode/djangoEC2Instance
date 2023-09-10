from django.shortcuts import render, redirect

from .forms import CreateUserForm
from django.contrib.auth.models import Group

from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(request):
    return render(request, 'formapp/index.html')

def register_view(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        print(form)
        print(form.is_valid())
        if form.is_valid():
            user = form.save()
            return redirect('/login')
    context = {'form': form}
    return render(request, 'formapp/register.html', context)

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'formapp/login.html', {'error': 'Invalid username or password.'})
    else:
        return render(request, 'formapp/login.html')
    
def logout_view(request):
    logout(request)
    return redirect('/login')