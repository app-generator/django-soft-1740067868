# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Team(models.Model):

    #__Team_FIELDS__
    name = models.TextField(max_length=255, null=True, blank=True)
    foundationdate = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Team_FIELDS__END

    class Meta:
        verbose_name        = _("Team")
        verbose_name_plural = _("Team")


class Player(models.Model):

    #__Player_FIELDS__
    name = models.TextField(max_length=255, null=True, blank=True)
    lastname = models.TextField(max_length=255, null=True, blank=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    age = models.IntegerField(null=True, blank=True)
    role = models.CharField(max_length=255, null=True, blank=True)

    #__Player_FIELDS__END

    class Meta:
        verbose_name        = _("Player")
        verbose_name_plural = _("Player")



#__MODELS__END
