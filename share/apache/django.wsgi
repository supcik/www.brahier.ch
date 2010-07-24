import os
import sys

sys.path.append(
    os.path.join(
        os.path.realpath(os.path.dirname(__file__)),
        "../../src"
    )
)

os.environ['DJANGO_SETTINGS_MODULE'] = 'brahier.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

