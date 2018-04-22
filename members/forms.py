from django import forms
from .models import Member

class AddMemberForm(forms.ModelForm):
    class Meta:
        model = Member
        # fields = ['first_name', 'last_name', 'mobile_number', 'email', 'address', 'subscription_type', 'subscription_period', 'amount']
        fields = '__all__'
        exclude = ['registration_upto']
        widgets = {
            'registration_date': forms.DateInput(attrs={'type': 'date'}),
            'registration_upto': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_mobile_number(self, *args, **kwargs):
        mobile_number = self.cleaned_data.get('mobile')
        if Member.objects.filter(mobile_number=mobile).exists():
            raise forms.ValidationError('This mobile number has already been registered.')
        else:
            return mobile_number

class UpdateMemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'