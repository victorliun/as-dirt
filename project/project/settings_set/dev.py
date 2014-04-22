try:
    from common import *
except ImportError:
    pass

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'django_quick_start',
        'USER': 'victor',
        'PASSWORD': 'lvxy',
        'HOST': '127.0.0.1',
        'PORT': '3306',    
    }
}
