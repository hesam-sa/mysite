from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from accounts.forms import CustomUserCreationForm
from django.contrib.auth.models import User



# Create your views here.
def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request,data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
            else:
                email = form.cleaned_data.get('username')
                form2 =User.objects.all()
                for fr in form2:
                    if email==fr.email:
                        username=fr.username
                password = form.cleaned_data.get("password")
            try:    
                user = authenticate(request,username=username,password=password)
                if user is not None:
                    login(request,user)
                    messages.add_message(request,messages.SUCCESS,'You are Logged In')
                    return redirect('/')
            except UnboundLocalError:
                messages.add_message(request,messages.ERROR,'Your username or password is Incorrect ')
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
