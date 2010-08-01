from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _

NAVIGATION = [
    ['home', _('Home'), '/', {'top' : 1}],
    ['webcam', _('Webcam'), '/webcam', {}],

    ['concours', _('Events'), '/concours', {}, [
        ['c_2010', '2010', '/concours/2010', {}],
        ['c_2009', '2009', '/concours/2009', {}],
    ]],
#    ['admin', _('Admin'), reverse('admin:index'), {}],
]
