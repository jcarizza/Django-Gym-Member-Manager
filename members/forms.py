"""Member forms."""

from django import forms
from django.utils.translation import ugettext_lazy as _
from members.models import Member


class AddMemberForm(forms.ModelForm):
    """Add a member form."""

    class Meta:  # pylint: disable=C0111
        model = Member
        fields = [
            'first_name',
            'last_name',
            'dni',
            'address',
            'email',
            'cellphone',
            'emergency_contact',
            'photo',
            'medical_certificate',
        ]
        widgets = {
            'registration_date': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'first_name': _('Nombre'),
            'last_name': _('Apellido'),
            'cellphone': _('Teléfono celular (opcional)'),
            'address': _('Dirección (opcional)'),
            'email': _('Email (opcional)'),
            'gym': _('Gimnasio'),
            'emergency_contact': _('Telefono en caso de urgencia (opcional)'),
            'photo': _('Foto del socio (opcional)'),
            'medical_certificate': _('Certificado médico (opcional)'),
            'dni': _('DNI')
        }
        help_texts = {
            'first_name': '',
            'last_name': '',
            'cellphone': '',
            'address': '',
            'photo': '',
            'emergency_contact': _('En caso de emergencia, nos comunicamos con este número.'),
            'email': _('Un email de contacto.'),
            'dni': _('Documento de identidad o número que identifique a esta persona.')
        }
