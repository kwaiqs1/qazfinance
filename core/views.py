from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Profile, Article
from .forms import CustomUserCreationForm, ProfileForm, ArticleForm


def home(request):
    """Home page with hero section and preview cards."""
    recent_articles = Article.objects.filter(for_students_only=False)[:3]
    upcoming_events = {
        'nfic': {
            'name': 'National Financial Intelligence Challenge (NFIC)',
            'status': 'Fundraising in progress',
            'budget_target': 750000,
        }
    }
    return render(request, 'core/home.html', {
        'recent_articles': recent_articles,
        'upcoming_events': upcoming_events,
    })


def our_mission(request):
    """Our Mission page."""
    return render(request, 'core/our_mission.html')


def what_we_do(request):
    """What We Do page."""
    articles_preview = Article.objects.all()[:6]
    return render(request, 'core/what_we_do.html', {
        'articles_preview': articles_preview,
    })


def upcoming_events(request):
    """Upcoming Events page."""
    return render(request, 'core/events.html')


def we_are_open(request):
    """We Are Open / Baqytty Shanyraq program page."""
    return render(request, 'core/we_are_open.html')


def we_are_looking_for(request):
    """Join the Team page."""
    return render(request, 'core/we_are_looking_for.html')


def blog_list(request):
    """Blog/Articles listing page."""
    articles = Article.objects.filter(for_students_only=False)
    category = request.GET.get('category', '')
    if category:
        articles = articles.filter(category=category)

    paginator = Paginator(articles, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'core/blog_list.html', {
        'page_obj': page_obj,
        'categories': Article.CATEGORY_CHOICES,
        'selected_category': category,
    })


def article_detail(request, slug):
    """Individual article detail page."""
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'core/article_detail.html', {'article': article})


def for_students(request):
    """For Students page with student-only articles."""
    articles = Article.objects.filter(for_students_only=True)
    paginator = Paginator(articles, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'core/for_students.html', {
        'page_obj': page_obj,
    })


def about_us(request):
    """About Us page."""
    return render(request, 'core/about.html')


def register(request):
    """User registration view."""
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Create profile for new user
            Profile.objects.create(
                user=user,
                full_name=user.username
            )
            messages.success(request, 'Registration successful! Please log in.')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'core/register.html', {'form': form})


def login_view(request):
    """User login view."""
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            next_url = request.GET.get('next', 'dashboard')
            return redirect(next_url)
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'core/login.html')


@login_required
def dashboard(request):
    """User dashboard."""
    articles_count = Article.objects.count()
    student_articles_count = Article.objects.filter(for_students_only=True).count()
    recent_articles = Article.objects.all()[:5]

    # Get user profile or create one
    profile, created = Profile.objects.get_or_create(user=request.user)

    return render(request, 'core/dashboard.html', {
        'articles_count': articles_count,
        'student_articles_count': student_articles_count,
        'recent_articles': recent_articles,
        'profile': profile,
    })


@login_required
def profile_view(request):
    """User profile view and edit."""
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'core/profile.html', {'form': form, 'profile': profile})

