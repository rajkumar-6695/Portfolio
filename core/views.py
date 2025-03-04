from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import PersonalInformation, Skill, Project, Service, Contact, Certificate
from .forms import UserRegistrationForm

def home(request):
    personal_info = PersonalInformation.objects.first()
    skills = Skill.objects.all()
    projects = Project.objects.all()
    services = Service.objects.all()
    certificates = Certificate.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        messages.success(request, 'Your message has been sent successfully!')
        return redirect('home')

    context = {
        'personal_info': personal_info,
        'skills': skills,
        'projects': projects,
        'services': services,
        'certificates': certificates,
    }
    return render(request, 'core/home.html', context)

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful. You can now login.')
            return redirect('admin:login')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})
