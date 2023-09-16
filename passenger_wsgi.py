# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/var/www/u0555309/data/www/fqf-nedvizhimost.ru')
sys.path.insert(1, '/var/www/u0555309/data/www/fqf-nedvizhimost.ru/myvenv/lib/python3.10/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'core.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()