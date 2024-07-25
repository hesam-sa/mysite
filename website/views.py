from django.shortcuts import render
from .forms import ContactForm,NewsForm

# Create your views here.
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect

def index_view(request):
    return render(request,'website/index.html')

def about_view(request):
    return render(request,'website/about.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
                        
    form=ContactForm()
    return render(request,'website/contact.html')

def newsletter_view(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/')