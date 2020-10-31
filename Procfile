
make sure to install 
gunicorn,request



web: gunicorn TechnicalRanjit.wsg
requirements.txt
STATIC_URL = '/static/'

STATIC_ROOT=os.path.join(BASE_DIR,'staticfiles')


    'django.middleware.security.SecurityMiddleware',
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

'whitenoise.runserver_nostatic',


from django.conf import settings
from django.conf.urls.static import static

+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
