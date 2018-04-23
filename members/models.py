"""Members models."""


from django.utils.translation import ugettext_lazy as _
from django.db import models
from members.mixins import (
    MembershipMixin,
    PersonalDetailsMixin,
)


class Gym(MembershipMixin):
    """A place, a gym."""
    name = models.CharField(
        max_length=100,
        help_text=_('Nombre del gimnasio')
    )
    address = models.CharField(
        max_length=100,
        help_text=_('Dirección')
    )


class GymActivity(models.Model):
    """Activities given by the gym."""


class StaffMember(PersonalDetailsMixin):
    """A staff member from a gym."""
    gym = models.ForeignKey(
        Gym,
        models.SET_NULL,
        blank=True,
        null=True,
        related_name='staff_members'
    )
    is_owner = models.NullBooleanField()


class Member(PersonalDetailsMixin):
    """A customer from a gym."""

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

    gym = models.ForeignKey(
        Gym,
        on_delete=models.CASCADE,
        help_text=_('Miembro del gimnasio')
    )

    emergency_contact = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text=_('Teéfono de contacto en caso de emergencia')
    )

    batch = models.CharField(
        max_length=30,
        choices=BATCH,
        default=BATCH[0][0],
        help_text=('Turno')
    )

    photo = models.FileField(
        upload_to='photos/',
        null=True,
        blank=True,
        help_text=_('Foto')
    )
    medical_certificate = models.FileField(
        upload_to='medical_certificate/',
        null=True,
        blank=True,
        help_text=_('Certificado médico')
    )

    dni = models.CharField(
        max_length=9,
        unique=True
    )

    # TODO: Implement subscriptions

    def __str__(self):
        return self.first_name + ' ' + self.last_name
