from pathlib import Path
import os, sys

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'u1ts-_)jnd7$ca=167=)*px1robsxp!fj2a^zr*(!hyutka7gl'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

sys.path.append(
    os.path.join(BASE_DIR, "apps")
)

# DEFAULT APP'S
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# EXTERN APP'S
INSTALLED_APPS += [
    'automated_logging',
]

# INTERN APP'S
INSTALLED_APPS += [
    'home',
    'usuarios',
    'receitas',
]

AUTH_USER_MODEL = "usuarios.Usuario"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'automated_logging.middleware.AutomatedLoggingMiddleware'
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                # LOCALIZAÇÃO VIEW BASE
                'home.views.base'
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static_files')
]

# STATIC_ROOT = os.path.join(BASE_DIR, 'static')

LOGIN_URL = "login"
LOGIN_REDIRECT_URL = "index"

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'file': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'warning.log',
        },
        'db': {
            'level': 'INFO',
            'class': 'automated_logging.handlers.DatabaseHandler',
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
        }
    },
    'loggers': {
        'automated_logging': {
            'level': 'INFO',
            'handlers': ['db'],
            'propagate': True,
        },
        'django': {
            'level': 'INFO',
            'handlers': ['console', 'db'],
            'propagate': True,
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        # notice the blank '', Usually you would put built in loggers like django or root here based on your needs
        '': {
            'handlers': ['file'], #notice how file variable is called in handler which has been defined above
            'level': 'WARNING',
            'propagate': True,
        },
    }
}

AUTOMATED_LOGGING = {
    "globals": {
        "exclude": {
            "applications": [
                "plain:contenttypes",
                "plain:admin",
                "plain:basehttp",
                "glob:session*",
                "plain:migrations",
            ]
        }
    },
    "model": {
        "detailed_message": True,
        "exclude": {"applications": [], "fields": [], "models": [], "unknown": False},
        "loglevel": 20,
        "mask": [],
        "max_age": None,
        "performance": True,
        "snapshot": True,
        "user_mirror": True,
    },
    "modules": ["request", "unspecified", "model"],
    "request": {
        "data": {
            "content_types": ["application/json"],
            "enabled": [],
            "ignore": [],
            "mask": ["password"],
            "query": False,
        },
        "exclude": {
            "applications": [],
            "methods": ["GET"],
            "status": [200],
            "unknown": False,
        },
        "ip": True,
        "loglevel": 20,
        "max_age": None,
    },
    "unspecified": {
        "exclude": {"applications": [], "files": [], "unknown": False},
        "loglevel": 20,
        "max_age": None,
    },
}


## -- Nome dos GRUPOS -- ##
GPMedico = "Médico"
GPPaciente = "Paciente"