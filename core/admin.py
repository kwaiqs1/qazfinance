from django.contrib import admin
from .models import Profile, Article, StudentResource, TeamMember


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'full_name', 'role', 'school', 'age', 'city']
    search_fields = ['user__username', 'full_name', 'city', 'school']
    list_filter = ['role']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'published_date', 'for_students_only']
    list_filter = ['category', 'for_students_only', 'published_date']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(StudentResource)
class StudentResourceAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'is_active', 'created_at']
    list_filter = ['is_active', 'category', 'created_at']
    search_fields = ['title', 'description', 'category']
    list_editable = ['is_active']


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'role', 'order']
    search_fields = ['name', 'role']
    list_editable = ['order']
    fields = ['name', 'role', 'bio', 'photo', 'order']

