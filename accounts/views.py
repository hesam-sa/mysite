from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from accounts.forms import CustomUserCreationForm



# Create your views here.
def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request,data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('/')

        form = AuthenticationForm()    
        context = {'form': form}
        return render(request,'accounts/login.html',context)
    else:
        return redirect('/')

@login_required(login_url='/accounts/login')
def logout_view(request):
    logout(request)
    return redirect('/')


def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'New User Submitted Successfully')
            return redirect('/accounts/login')
            
        else:
            messages.add_message(request,messages.ERROR,'New User Not Submitted ')
            return redirect('/')
            
    form = CustomUserCreationForm()
    context = {'form': form}
    return render(request,'accounts/signup.html',context)
