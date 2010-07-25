from django.conf import settings

def version(request):
    return {'portal_version': settings.VERSION}
