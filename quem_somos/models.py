from django.db import models
from django.utils.translation import ugettext_lazy as _


class Person(models.Model):
    name = models.CharField(_('Name'), max_length=255)
    bio = models.TextField(_('Biography'), blank=True)
    lattes = models.URLField(_('CV'), null=True, blank=True)
    photo = models.ImageField(_('Photo'), upload_to='photo/', blank=True, null=True)
    coordination = models.BooleanField(_('Coordination'), default=False)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('Person')
        verbose_name_plural = _('People')
