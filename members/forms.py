from django import forms
from .models import Member


class AddMemberForm(ModelForm):
    class Meta:
        model = Member
        fields = '__all__'
        exclude = ['registration_upto']
        widgets = {
            'registration_date': forms.DateInput(attrs={'type': 'date'}),
            'registration_upto': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_mobile_number(self, *args, **kwargs):
        mobile_number = self.cleaned_data.get('mobile_number')
        if Member.objects.filter(mobile_number=mobile_number).exists():
            raise forms.ValidationError('This mobile number has already been registered.')
        else:
            return mobile_number


class SearchForm(forms.Form):
        search = forms.CharField(label='Search Member', max_length=100)

class UpdateMemberForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    registration_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    registration_upto = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    subscription_type  = forms.ChoiceField(choices=SUBSCRIPTION_TYPE_CHOICES)
    subscription_period = forms.ChoiceField(choices=SUBSCRIPTION_PERIOD_CHOICES)
    fee_status = forms.ChoiceField(choices=FEE_STATUS)
    amount = forms.IntegerField()
    photo = forms.FileField(label='Update Photo', required=False)