from django.contrib import admin
from .models import Profile, Article


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'full_name', 'role', 'city']
    search_fields = ['user__username', 'full_name', 'city']
    list_filter = ['role']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'published_date', 'for_students_only']
    list_filter = ['category', 'for_students_only', 'published_date']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}

