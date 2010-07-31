from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.views import login, logout, \
  password_change, password_change_done

admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^brahier/', include('brahier.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    (r'^$',       'brahier.www.views.static', {'file' : 'www/index.html'}),
    (r'^webcam$', 'brahier.www.views.static', {'file' : 'www/webcam.html'}),
    (r'^accounts/login/$', login),
    (r'^accounts/logout/$', logout, {'next_page': '/'}),
    (r'^accounts/passwd/$', password_change),
    (r'^accounts/passwd/changed$', password_change_done),
    (r'^accounts/profile/$', 'brahier.account.views.profile'),
    (r'^admin/', include(admin.site.urls)),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),

)
