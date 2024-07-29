from django.shortcuts import render
from .forms import ContactForm,NewsForm

# Create your views here.
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from django.contrib import messages

def index_view(request):
    return render(request,'website/index.html')

def about_view(request):
    return render(request,'website/about.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.name = 'anonymous'
            instance.save()
            
            messages.add_message(request,messages.SUCCESS,'Your Ticket Submitted Successfully')
        else:
            messages.add_message(request,messages.ERROR,'Your Ticket Not Submitted ')
                        
    form=ContactForm()
    context = {'form':form}
    return render(request,'website/contact.html',context)

def newsletter_view(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/')