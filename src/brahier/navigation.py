from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _

NAVIGATION = [
    ['home', _('Accueil'), '/', {'top' : 1}],
    ['webcam', _('Webcam'), '/webcam', {}],

    ['concours', _('Concours'), '/concours', {}, [
        ['c_2010', _('2010'), '/concours/2010', {}],
        ['c_2009', _('2009'), '/concours/2009', {}],
    ]],
#    ['admin', _('Admin'), reverse('admin:index'), {}],
]
