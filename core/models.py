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
    full_name = models.CharField(max_length=200)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default='Student')
    bio = models.TextField(blank=True)
    city = models.CharField(max_length=100, blank=True)
    school = models.CharField(max_length=200)
    age = models.PositiveIntegerField()
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


class StudentResource(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=100, blank=True, help_text="e.g. 'Course', 'Program', 'Competition'")
    link = models.URLField(blank=True, help_text="Optional external link")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=150)
    bio = models.TextField(blank=True)
    photo = models.ImageField(
        upload_to="team_photos/",
        blank=True,
        null=True,
        help_text="Upload a portrait photo for this team member."
    )
    photo_path = models.CharField(
        max_length=255,
        blank=True,
        help_text="Static path relative to the 'core' static folder, e.g. 'core/images/team/nursaya.jpg' (deprecated, use photo field instead)"
    )
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "name"]

    def __str__(self):
        return f"{self.name} - {self.role}"

