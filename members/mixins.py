"""Members app mixins."""

from django.db import models
from django.utils.translation import ugettext_lazy as _


class PersonalDetailsMixin(models.Model):
    """Common personal details."""
    first_name = models.CharField(
        max_length=50,
        help_text=_('Nombre'))
    last_name = models.CharField(
        max_length=50,
        help_text=_('Apellido'))
    cellphone = models.CharField(
        max_length=50,
        help_text=_('Teléfono Celular')
    )
    address = models.CharField(
        max_length=100,
        help_text=_('Dirección')
    )
    email = models.EmailField()

    class Meta:  # pylint: disable=C0111
        abstract = True


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

    class Meta: # pylint: disable=C0111
        abstract = True
