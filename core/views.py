from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.http import FileResponse, Http404
from .models import Profile, Project, Experience, ContactMessage
from django.contrib import messages

def home(request):
    profile = Profile.objects.first()
    return render(request, 'home.html', {'profile': profile})

def about(request):
    profile = Profile.objects.first()
    return render(request, 'about.html', {'profile': profile})

def experience(request):
    experiences = Experience.objects.all()
    return render(request, 'experience.html', {'experiences': experiences})

def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects})

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        
        try:
            send_mail(
                f"New Portfolio Message: {subject}",
                f"From: {name} ({email})\n\nMessage:\n{message}",
                settings.DEFAULT_FROM_EMAIL,
                [settings.DEFAULT_FROM_EMAIL],
                fail_silently=False,
            )
            messages.success(request, "Your message has been sent successfully!")
        except Exception:
            messages.error(request, "There was an error sending your message.")
            
        return redirect('contact')
    return render(request, 'contact.html')

def download_resume(request):
    profile = Profile.objects.first()
    if profile and profile.resume:
        response = FileResponse(profile.resume.open(), content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{profile.resume.name.split("/")[-1]}"'
        return response
    raise Http404("Resume not found")
