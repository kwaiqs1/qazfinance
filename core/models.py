from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Profile(models.Model):
    ROLE_CHOICES = [
        ('Student', 'Student'),
        ('Mentor', 'Mentor'),
        ('SMM', 'SMM'),
        ('Tech', 'Tech'),
        ('Sponsor', 'Sponsor'),
        ('Other', 'Other'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    full_name = models.CharField(max_length=200, blank=True)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default='Student')
    bio = models.TextField(blank=True)
    city = models.CharField(max_length=100, blank=True)
    school = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.full_name or self.user.username}'s Profile"

    def get_absolute_url(self):
        return reverse('profile')


class Article(models.Model):
    CATEGORY_CHOICES = [
        ('Investing', 'Investing'),
        ('Personal Finance', 'Personal Finance'),
        ('Economics', 'Economics'),
        ('Financial Literacy', 'Financial Literacy'),
        ('News', 'News'),
        ('Other', 'Other'),
    ]

    title = models.CharField(max_length=300)
    slug = models.SlugField(unique=True, max_length=300)
    published_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Financial Literacy')
    description = models.TextField(help_text="Short description/preview")
    content = models.TextField(help_text="Full article content")
    for_students_only = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)

    class Meta:
        ordering = ['-published_date']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'slug': self.slug})

