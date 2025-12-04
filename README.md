# QazFinance Website

Kazakhstan's first teen-founded, nonprofit educational organization dedicated to financial literacy and investing.

## Project Overview

This is a complete Django-based website for QazFinance, featuring:

- User authentication and profiles
- Blog/Articles system
- Dashboard for logged-in users
- Event management pages
- Responsive mobile-first design
- Modern UI with smooth animations

## Technology Stack

- **Backend**: Django 5.0+
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Database**: SQLite (development)

## Setup Instructions

### 1. Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### 2. Installation

1. **Clone or navigate to the project directory**:
   ```bash
   cd QazFinance
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

### 3. Database Setup

1. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

2. **Create a superuser** (for admin access):
   ```bash
   python manage.py createsuperuser
   ```
   Follow the prompts to create an admin account.

3. **Create sample articles** (optional):
   ```bash
   python manage.py create_sample_articles
   ```

### 4. Run the Development Server

```bash
python manage.py runserver
```

The site will be available at `http://127.0.0.1:8000/`

## Project Structure

```
QazFinance/
├── qazfinance_site/          # Main Django project
│   ├── settings.py           # Project settings
│   ├── urls.py               # Main URL configuration
│   └── wsgi.py               # WSGI configuration
├── core/                     # Main application
│   ├── models.py             # Database models (Profile, Article)
│   ├── views.py              # View functions
│   ├── urls.py               # App URL configuration
│   ├── forms.py              # Form definitions
│   ├── admin.py              # Admin configuration
│   ├── templates/            # HTML templates
│   │   └── core/
│   │       ├── base.html     # Base template
│   │       ├── home.html     # Home page
│   │       ├── dashboard.html
│   │       └── ...           # Other templates
│   └── static/               # Static files
│       └── core/
│           ├── css/
│           │   └── main.css  # Main stylesheet
│           └── js/
│               └── main.js   # Main JavaScript
├── manage.py                 # Django management script
├── requirements.txt          # Python dependencies
└── README.md                 # This file
```

## Features

### Public Pages

- **Home**: Hero section, main pillars, preview cards
- **Our Mission**: Mission statement and goals
- **What We Do**: Detailed breakdown of activities
- **Upcoming Events**: NFIC and other events
- **We Are Open**: Baqytty Shanyraq program
- **We Are Looking For**: Join the team page
- **Blog**: Article listings with categories
- **For Students**: Student-specific articles
- **About Us**: Organization information

### Authentication

- User registration
- Login/Logout
- User profiles with editable information
- Role selection (Student, Mentor, SMM, Tech, Sponsor, Other)

### Dashboard

- Overview cards with statistics
- Highlight cards for main projects
- Recent articles list
- Sidebar navigation

## Design Features

- **Color Palette**:
  - Primary: Deep navy (#1a2744)
  - Secondary: Light blue (#4a90e2)
  - Accent: Soft green (#6bcf7f), Teal (#2ec4b6)

- **Responsive Design**:
  - Mobile-first approach
  - Desktop sidebar navigation
  - Mobile overlay menu
  - Fully responsive layouts

- **Animations**:
  - Scroll-triggered fade-in/slide-up
  - Smooth transitions
  - Hover effects
  - Progress bar animations

## Admin Panel

Access the Django admin panel at `http://127.0.0.1:8000/admin/` using your superuser credentials.

From the admin panel, you can:
- Manage articles
- View/edit user profiles
- Add/edit content

## Creating Sample Data

To create sample articles for testing:

```bash
python manage.py create_sample_articles
```

This will create 3 sample articles:
- "How to Start Investing as a Teenager"
- "Basics of Budgeting for Students"
- "What Is Financial Literacy and Why Does It Matter?"

## Development Notes

- Static files are served automatically in development
- CSRF protection is enabled
- User authentication uses Django's built-in system
- All forms include validation

## Production Deployment

Before deploying to production:

1. Set `DEBUG = False` in `settings.py`
2. Update `SECRET_KEY` with a secure random key
3. Configure `ALLOWED_HOSTS`
4. Set up proper static file serving
5. Use a production database (PostgreSQL recommended)
6. Set up proper media file storage

## Support

For issues or questions, please contact the QazFinance team.

---

**Built with ❤️ for financial literacy education in Kazakhstan**

