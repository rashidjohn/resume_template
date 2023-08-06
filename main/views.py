from django.shortcuts import render,redirect
from .models import *
from .forms import ContactForm
from django.contrib import messages

# Create your views here.
def index(request):
    form = ContactForm()
    about = About_me.objects.all()
    skills = Skill.objects.all()
    expericence = Expericence.objects.all()
    services = Service.objects.all()
    portfolio = Portfolio.objects.all()
    form = ContactForm()
    testimonial = Testimonial.objects.all()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Xabar yuborildi!✔️")
            return redirect('index')
    form = ContactForm()
    context = {
        'about':about,
        'skills':skills,
        'expericence':expericence,
        'services':services,
        'portfolio':portfolio,
        'form':form,
        'testimonial':testimonial
    }
    return render(request, 'index.html', context)