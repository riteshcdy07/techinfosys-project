from django.db import models

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    # Fixed indentation below (now exactly 4 spaces)
    image = models.ImageField(
        upload_to='core/images/icons/', 
        null=True, 
        blank=True, 
        help_text="Upload a logo or icon image (PNG/SVG recommended)"
    )

    def __str__(self):
        return self.title

class Technology(models.Model):
    name = models.CharField(max_length=100)
    # This field is correctly indented
    image = models.ImageField(upload_to='tech_logos/', null=True, blank=True)
    category = models.CharField(max_length=100, choices=[
        ('Web Development', 'Web Development'),
        ('App Development', 'App Development'),
        ('Database', 'Database'),
        ('Cloud Platform', 'Cloud Platform'),
    ])

    def __str__(self):
        return self.name
    

from django.db import models


class ContactMessage(models.Model):
    SERVICE_CHOICES = [
        ("Web Development", "Web Development"),
        ("App Development", "App Development"),
        ("SEO", "SEO"),
        ("UI/UX", "UI/UX"),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    service = models.CharField(
        max_length=100,
        choices=SERVICE_CHOICES,
        blank=True
    )
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.service or 'General Enquiry'}"