from django.db import models
from django.utils.translation import ugettext_lazy as _


class Interest(models.Model):
    name = models.CharField(_('Name'), max_length=255)

    def __unicode__(self):
        return self.name


class Schooling(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class Person(models.Model):
    select_interest = models.ForeignKey(Interest, verbose_name=_('Interest'), null=True, blank=True)
    schooling = models.ForeignKey(Schooling, verbose_name=_('Schooling'), null=True, blank=True)
    full_name = models.CharField(_('Name'), max_length=255)
    email = models.EmailField(_('Email'), unique=True)
    birth = models.DateField(_('Date of birth'), null=True, blank=True)
    note = models.TextField(_('How did you hear about the project?'), blank=True)
    zipcode = models.CharField(_('Zip Code'), max_length=9, blank=True)
    street = models.CharField(_('Address'), max_length=255, blank=True)
    street_complement = models.CharField(_('Complement'), max_length=255, blank=True)
    number = models.CharField(_('Number'), max_length=10, blank=True)
    district = models.CharField(_('District'), max_length=255, blank=True)
    city = models.CharField(_('City'), max_length=255, blank=True)
    state = models.CharField(_('State'), max_length=255, blank=True)
    country = models.CharField(_('Country'), max_length=255, blank=True)

    def __unicode__(self):
        return self.full_name
