# Quick Setup Guide

## Installation Steps

1. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run database migrations:**
   ```bash
   python manage.py migrate
   ```

3. **Create a superuser (admin account):**
   ```bash
   python manage.py createsuperuser
   ```

4. **Create sample articles (optional):**
   ```bash
   python manage.py create_sample_articles
   ```

5. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

6. **Access the site:**
   - Homepage: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

## First Steps After Setup

1. Log into the admin panel with your superuser credentials
2. Review the sample articles (if created)
3. Create a test user account through the registration page
4. Explore the dashboard after logging in
5. Customize content through the admin panel

## Common Commands

```bash
# Run migrations
python manage.py migrate

# Create migrations (if models change)
python manage.py makemigrations

# Collect static files (for production)
python manage.py collectstatic

# Create sample data
python manage.py create_sample_articles

# Run development server on specific port
python manage.py runserver 8080
```

## Troubleshooting

**Issue: Static files not loading**
- Make sure `STATIC_URL` and `STATICFILES_DIRS` are configured in settings.py
- In development, Django serves static files automatically
- Run `python manage.py collectstatic` only in production

**Issue: Database errors**
- Delete `db.sqlite3` and run `python manage.py migrate` again
- Make sure you've run migrations: `python manage.py migrate`

**Issue: Template errors**
- Check that all templates are in `core/templates/core/`
- Verify template names match the views

**Issue: Import errors**
- Activate your virtual environment
- Reinstall dependencies: `pip install -r requirements.txt`

## Next Steps

1. Customize the content in the admin panel
2. Add more articles through the admin
3. Update team member information in About Us section
4. Configure email settings for production
5. Set up proper media file handling if needed

