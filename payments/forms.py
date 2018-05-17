import datetime

from django import forms
from django.forms import ValidationError
from django.utils.translation import gettext as _

from .models import Payments
from members.models import Member


PAYMENT_PERIOD_CHOICES = (
    (1, _('1 Mes')),
    (2, _('2 Meses')),
    (3, _('3 Meses')),
    (4, _('4 Meses')),
    (5, _('5 Meses')),
    (6, _('6 Meses')),
    (7, _('7 Meses')),
    (8, _('8 Meses')),
    (9, _('9 Meses')),
    (10, _('10 Meses')),
    (11, _('11 Meses')),
    (12, _('12 Meses'))
)


class AddPaymentWithDNIForm(forms.ModelForm):
    dni = forms.CharField()
    payment_period = forms.ChoiceField(choices=PAYMENT_PERIOD_CHOICES)

    class Meta:
        model = Payments
        fields = ('dni', 'payment_period', 'payment_amount')

    def clean_dni(self):
        value = self.cleaned_data['dni']
        if not Member.objects.filter(dni=value).exists():
            raise ValidationError(_('Member not found'))
        return value

    def save(self):
        member_dni = self.cleaned_data.pop('dni')
        member = Member.objects.get(dni=member_dni)
        return Payments.objects.create(user=member,
                                       payment_date=datetime.datetime.now(),
                                       **self.cleaned_data)

class AddPaymentForm(forms.ModelForm):
    payment_period = forms.ChoiceField(choices=PAYMENT_PERIOD_CHOICES)
    
    class Meta:
        model = Payments
        fields = ('payment_period', 'payment_amount')
