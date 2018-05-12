"""Members models."""


from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.db import models


class Gym(models.Model):
    """A place, a gym."""
    name = models.CharField(
        max_length=100,
        help_text=_('Nombre del gimnasio')
    )
    address = models.CharField(
        max_length=100,
        help_text=_('Dirección')
    )
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"


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


class Member(models.Model):
    """A customer from a gym."""

    gym = models.ForeignKey(
        Gym,
        on_delete=models.CASCADE,
        help_text=_('Miembro del gimnasio')
    )

    first_name = models.CharField(
        max_length=50,
        help_text=_('Nombre'))

    last_name = models.CharField(
        max_length=50,
        help_text=_('Apellido'))

    cellphone = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text=_('Teléfono Celular')
    )

    address = models.CharField(
        blank=True,
        null=True,
        max_length=100,
        help_text=_('Dirección')
    )

    email = models.EmailField(
        blank=True,
        null=True,
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


class Feedback(models.Model):
    """An user send us a suggestion."""
    text = models.TextField()
    user = models.ForeignKey(StaffMember, on_delete=models.CASCADE)
    on_date = models.DateTimeField(auto_now_add=True)
    checked = models.NullBooleanField()

    def __str__(self):
        return f"{self.id}"  # pylint: disable=E1101
