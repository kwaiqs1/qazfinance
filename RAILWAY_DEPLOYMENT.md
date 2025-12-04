# Railway.app Deployment Configuration

This document summarizes all changes made to prepare the QazFinance Django project for deployment on Railway.app.

## Files Changed/Created

### 1. **Procfile** (NEW)
- Created in project root
- Contains: `web: gunicorn qazfinance_site.wsgi:application`
- Tells Railway how to run the application

### 2. **requirements.txt** (UPDATED)
Added deployment dependencies:
- `gunicorn` - WSGI HTTP server for production
- `whitenoise` - Static file serving middleware
- `dj-database-url` - Database URL parsing
- `psycopg2-binary` - PostgreSQL adapter for Python

### 3. **qazfinance_site/settings.py** (UPDATED)
Major changes for production deployment:

#### Imports Added:
- `import dj_database_url` - For database URL parsing

#### Environment-Based Configuration:
- **SECRET_KEY**: Now reads from `SECRET_KEY` environment variable
- **DEBUG**: Reads from `DEBUG` environment variable (defaults to `False`)
- **ALLOWED_HOSTS**: Set to `["*"]` to allow Railway domain

#### Middleware Updates:
- Added `whitenoise.middleware.WhiteNoiseMiddleware` right after `SecurityMiddleware`

#### Database Configuration:
- Uses `dj_database_url` to parse `DATABASE_URL` environment variable
- Falls back to SQLite locally if `DATABASE_URL` is not set
- Automatically enables SSL requirement for PostgreSQL connections
- Includes connection pooling settings (`conn_max_age=600`, `conn_health_checks=True`)

#### Static Files Configuration:
- `STATIC_ROOT` already set to `BASE_DIR / 'staticfiles'`
- `STATICFILES_DIRS` configured for `collectstatic`
- Added `STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'` for optimized static file serving

### 4. **core/templates/core/login.html** (RECREATED)
- Recreated the missing login template that was accidentally deleted

## Environment Variables to Set in Railway

You'll need to set these environment variables in your Railway project:

1. **SECRET_KEY** (Required)
   - Generate a secure random key
   - You can generate one with: `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"`

2. **DEBUG** (Optional)
   - Set to `True` for debugging (not recommended in production)
   - Defaults to `False` if not set

3. **DATABASE_URL** (Automatically set by Railway)
   - Railway automatically provides this when you add a PostgreSQL database
   - No manual configuration needed

## Deployment Checklist

- [x] Procfile created with gunicorn command
- [x] All required packages added to requirements.txt
- [x] DEBUG configured from environment variable
- [x] ALLOWED_HOSTS configured for Railway
- [x] Database configuration using dj-database_url
- [x] WhiteNoise middleware added
- [x] WhiteNoise static file storage configured
- [x] STATIC_ROOT and STATICFILES_DIRS configured
- [x] SSL required for PostgreSQL connections

## Next Steps for Railway Deployment

1. **Push code to Git repository** (GitHub, GitLab, etc.)

2. **Create Railway project:**
   - Go to https://railway.app
   - Create new project
   - Connect your repository

3. **Add PostgreSQL database:**
   - In Railway dashboard, click "New" → "Database" → "Add PostgreSQL"
   - Railway will automatically set `DATABASE_URL` environment variable

4. **Set environment variables:**
   - Go to project settings → Variables
   - Add `SECRET_KEY` with a secure random key
   - Optionally set `DEBUG=False` (it's the default)

5. **Deploy:**
   - Railway will automatically detect the Procfile
   - It will run `pip install -r requirements.txt`
   - It will run migrations automatically (if configured)
   - Your app will be live!

6. **Run migrations (if not automatic):**
   - Railway CLI: `railway run python manage.py migrate`
   - Or add a build script in Railway

7. **Create superuser (optional):**
   - Railway CLI: `railway run python manage.py createsuperuser`

## Important Notes

- **Static Files**: WhiteNoise will serve static files directly from Django, so no separate static file hosting needed
- **Database**: Railway automatically provides PostgreSQL with `DATABASE_URL` set
- **Security**: Make sure to set a strong `SECRET_KEY` in production
- **Debug Mode**: Keep `DEBUG=False` in production for security

## Local Development

The configuration still works locally:
- Uses SQLite by default when `DATABASE_URL` is not set
- `DEBUG=True` can be set locally via environment variable
- All static files work with `python manage.py runserver`

Your project is now ready for Railway deployment! 🚀

