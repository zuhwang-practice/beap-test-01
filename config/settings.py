"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# 프로젝트 루트 폴터 설정파일이나 py파일등에서 프로젝트의 루트 폴더를 찾아 그 하위를 탐색한다거나 하는 일들을 빈번하게 수행한다.
# 이때문에 변수로 미리 준비해 두는 값
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# 시크릿 키는 다양한 보안을 위해 사용된다. 세션값의 보호나 비밀번호 변경시 사용되는 보안url을 만드는 등의 일을 주로 사용.
# 임의로 변경할 수 있으나 변경하면 로그인이 풀리는 등 부작용이 있다. 또 정해진 값을 외부에 노출되면 절대 안된다! 보안 문제!
SECRET_KEY = 'q*acd0+5ipozx23ns@8wyz_w88_zu0k$^o*z-^8o6=3=ll*@dl'

# SECURITY WARNING: don't run with debug turned on in production!
# 디버그 모드를 설정, 참일때 다양한 오류 메세지를 즉시 확인 할 수 있다.
# 실제로 배포할 때는 false로 바꾸어 사용하며 이때는 다른 설정값을 이용해 관리자가 오류 메세지를 보게 설정 할 수 있다.
DEBUG = False


# 현재 서비스의 호스트를 설정한다. 개발시에는 비어두고 사용하나, 배포시에는 '*' 나 실제 도메인을 기록한다.
# '*' 는 모든도메인을 나타내는데 보안상 위험하기 때문에 실제 도메인을 작성하도록 권장한다.
# 이는 DNS Rebinding을 막기위한 조치이며, DEBUG 모드가 false일때 ALLOWED_HOSTS 값이 비어있다면 서비스를 할 수 없다. 주의!
ALLOWED_HOSTS = ['*']


# Application definition

# 장고 웹 서비스는 다양한 앱의 결합으로 만들어진다. 현재프로젝트에서 사용하는 앱의 목록을 기록하고 관리하는 설정으로
# 나중에 직접 만들 앱들도 여기에 기록해야 한다.
INSTALLED_APPS = [
    'polls.apps.PollsConfig',
    'bookmark.apps.BookmarkConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# 미들웨어는 장고의 모든 요청/응답 메세지 사이에 실행되는 특수한 프레임워크를 말한다.
# 주로 보안에 관한 내용이 많다.
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 기준이 되는 urls.py 파일의 경로를 설정한다. = 최상위 urls
ROOT_URLCONF = 'config.urls'

# 장고에서 사용하는 템플릿 시스템에 관한 설정
# 템플릿 해석 앤진과 템플릿 폴더 경로등을 변경할떼 쓰인다.
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # 프로젝트 루트 경로에 템플릿츠 폴더적용
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# 실행을 위한 WSGI 어플리케이션을 설정한다.
WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# 데이터베이스 관련 설정. 만약 mysql사용할거면 변경해야 한다.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

# 비밀번호 검증을 위한 설정, 기본적으로 들어있는 검증규칙은 사용자 정보와 유사한지, 숫자로만 만들었는지, 너무 짧은지, 평범한 비밀번호인지 검증하도록 되어 있다.
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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

# 이하 다국어에 관한 설정
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

# 각 어플리케이션 폴더 아래 static 폴더에 정적파일을 넣어 보관할수 있다.
STATIC_URL = '/static/'

# 프로젝트 루트 경로에 static폴더를 지정한다.
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
