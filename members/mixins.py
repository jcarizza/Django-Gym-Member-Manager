"""Members app mixins."""

from django.db import models
from django.utils.translation import ugettext_lazy as _


class MembershipMixin(models.Model):
    """Membership fields."""

    MEMBERSHIP_STATUS_CHOICES = (
        ('paid', _('Pago')),
        ('pending', _('Pendiente')),
    )

    status = models.CharField(
        max_length=30,
        choices=MEMBERSHIP_STATUS_CHOICES,
        default=MEMBERSHIP_STATUS_CHOICES[0][0]
    )
    registration_date = models.DateField()
    registration_upto = models.DateField()

    class Meta:
        abstract = True