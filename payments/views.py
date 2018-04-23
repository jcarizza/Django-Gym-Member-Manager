from django.views.generic.edit import FormView

from .forms import PaymentsForm


class CreatePaymentView(FormView):
    form_class = PaymentsForm
    template_name = 'add_payment.html'
    success_url = '/members'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
