from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _

NAVIGATION = [
    ['home', _('Home RA Portal'), '/', {'top' : 1}],
    ['reg', _('Registration'), None, {}, [
        ['reg_whois', _('Whois'), {}, '/'],
        ['reg_search_cert', _('Search Certificate'), {}, '/'],
        ['reg_decode_req', _('Decode/Check CSR'), {}, '/'],
        ['reg_decode_cert', _('Decode Cert'), {}, '/'],
    ]],
    ['doc', _('Documents'), None, {}, [
        ['doc_manual', _('Documents/Manuals'), {}, '/'],
        ['doc_faq', _('F.A.Q.'), {}, '/'],
        ['doc_news', _('News'), {}, '/'],
    ]],
    ['fmh', _('FMH'), None, {}, [
        ['fmh_revoke', _('Revoke'), {}, '/'],
    ]],
    ['admin', _('Admin'), {}, reverse('admin:index')],
]
