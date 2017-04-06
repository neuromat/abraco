from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _


class RegistrationApp(CMSApp):
    name = _("Registration")
    urls = ['faca_parte.urls', ]
    app_name = 'faca_parte'

apphook_pool.register(RegistrationApp)
