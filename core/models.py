from django.db import models
from django.core.validators import FileExtensionValidator

class Profile(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField()
    profile_image = models.ImageField(upload_to='profile/')
    resume = models.FileField(
        upload_to='resumes/',
        validators=[FileExtensionValidator(allowed_extensions=['pdf'])]
    )
    email = models.EmailField()
    github = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    link = models.URLField(max_length=500, blank=True, null=True)
    github_link = models.URLField(max_length=500, blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

class Experience(models.Model):
    company = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField()
    is_current = models.BooleanField(default=False)

    class Meta:
        ordering = ['-start_date']

    def __str__(self):
        return f"{self.position} at {self.company}"

class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"
