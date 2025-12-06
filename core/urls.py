from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Public pages
    path('', views.home, name='home'),
    path('our-mission/', views.our_mission, name='our_mission'),
    path('what-we-do/', views.what_we_do, name='what_we_do'),
    path('upcoming-events/', views.upcoming_events, name='events'),
    path('we-are-open/', views.we_are_open, name='we_are_open'),
    path('we-are-looking-for/', views.we_are_looking_for, name='we_are_looking_for'),
    # path('blog/', views.blog_list, name='blog_list'),  # Blog temporarily disabled
    path('article/<slug:slug>/', views.article_detail, name='article_detail'),
    path('for-students/', views.for_students, name='for_students'),
    path('about/', views.about_us, name='about'),

    # Authentication
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Dashboard and profile (requires login)
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.profile_view, name='profile'),
]

