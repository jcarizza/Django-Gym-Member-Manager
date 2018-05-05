"""Members models."""


from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser
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


class StaffMember(AbstractUser):
    """A staff member from a gym."""
    gym = models.ForeignKey(
        Gym,
        models.SET_NULL,
        blank=True,
        null=True,
        related_name='staff_members'
    )
    is_owner = models.NullBooleanField()
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['gym', 'is_owner', 'first_name', 'last_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Member(PersonalDetailsMixin):
    """A customer from a gym."""

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
