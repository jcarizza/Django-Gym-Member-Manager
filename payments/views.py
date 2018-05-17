from django.views.generic.edit import FormView

from .forms import AddPaymentWithDNIForm


class CreatePaymentView(FormView):
    form_class = AddPaymentWithDNIForm
    template_name = 'add_payment.html'
    success_url = '/members'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
