# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.mysql',
       'NAME': 'stepic_web',
       'USER': 'root',
       'PASSWORD': '',
       'HOST': '127.0.0.1',
       'PORT': '3306',
   }
}