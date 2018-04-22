from django.utils.translation import ugettext_lazy as _
from django.forms import ModelForm
from django.db import models
from django import forms
from members.mixins import MembershipMixin

import datetime


class Gym(MembershipMixin):
    """A place, a gym."""
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=300, blank=True)


class Subscription(models.Model):
    """Subscription."""
    name = models.CharField(max_length=100)


class Member(MembershipMixin):

    BATCH = (
        ('morning', _('Mañana')),
        ('evening', _('Tarde')),
        ('night', _('Noche')),
        ('full', _('Fulltime')),
    )

    SUBSCRIPTION_PERIOD_CHOICES = (
        ('1', '1 Month'),
        ('3', '3 Months'),
        ('6', '6 Months'),
        ('12', '12 Months'),
    )

    # Personal info
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mobile = models.IntegerField(unique=True)
    emerency_contact = models.IntegerField(blank=True, null=True)
    email = models.EmailField(null=True, blank=True)
    address = models.CharField(max_length=300, blank=True)

    # Subscription
    subscription_type = models.ForeignKey(
        Subscription,
        models.SET_NULL,
        blank=True, null=True
    )
    subscription_period = models.CharField(
        max_length=30,
        choices=SUBSCRIPTION_PERIOD_CHOICES,
        default=SUBSCRIPTION_PERIOD_CHOICES[0][0]
    )
    batch = models.CharField(
        max_length=30,
        choices=BATCH,
        default=BATCH[0][0]
    )
    photo = models.FileField(upload_to='photos/', blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
