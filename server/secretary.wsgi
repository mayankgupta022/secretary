import os
import sys	
sys.path.append('~/media/mayank/djcode/secretary/secretary/server/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'secretary.settings'
#import django.core.handlers.wsgi
#application = django.core.handlers.wsgi.WSGIHandler()

import django.core.wsgi
application = django.core.wsgi.get_wsgi_application()