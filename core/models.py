from django.db import models
from ckeditor.fields import RichTextField

class PersonalInformation(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    description = RichTextField()
    about = RichTextField(null=True, blank=True, help_text='Content for About section')
    profile_image = models.ImageField(upload_to='profile/')
    cv_file = models.FileField(upload_to='cv/', null=True, blank=True)
    github = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    youtube = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Personal Information'

class Skill(models.Model):
    name = models.CharField(max_length=100)
    percentage = models.IntegerField()

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField()
    image = models.ImageField(upload_to='projects/')
    url = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']

class Service(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField()
    icon = models.CharField(max_length=100, help_text='Font Awesome class name')

    def __str__(self):
        return self.title

class Certificate(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField()
    image = models.ImageField(upload_to='certificates/')
    date_received = models.DateField()
    issuing_organization = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_received']

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.subject}'

    class Meta:
        ordering = ['-created_at']
