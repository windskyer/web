from __future__ import unicode_literals

import datetime

from django.utils import timezone
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext, ugettext_lazy as _

from django.utils import timezone


# Create your models here.

@python_2_unicode_compatible
class Userinfo(models.Model):

    username = models.CharField(_('username'), max_length=128, null=True)
    firstname = models.CharField(max_length=200, null=True)
    lastname = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    department = models.CharField(max_length=200, null=True)
    company = models.CharField(max_length=200, null=True)
    workphone = models.CharField(max_length=200, null=True)
    homephone = models.CharField(max_length=200, null=True)
    mobilephone = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    country = models.CharField(max_length=200, null=True)
    zip = models.CharField(max_length=200, null=True)
    notes = models.CharField(max_length=200, null=True)
    changeuserinfo = models.CharField(max_length=128, null=True)
    portalloginpassword = models.CharField(max_length=128, null=True)
    enableportallogin = models.IntegerField(default=0)
    creationdate = models.DateTimeField(auto_now=True)
    creationby = models.TextField(max_length=200, default=timezone.now)
    updatedate = models.DateTimeField(_('update date'), null=True)
    updateby = models.TextField(max_length=200, null=True)

    class Meta:
        db_table = _('userinfo')
        verbose_name = _('userinfo')

    def __str__(self):
        return self.username
