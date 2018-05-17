"""Members views."""

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import (
    TemplateView,
    View
)
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    FormView,
)
from members.models import (
    Member,
    Feedback,
)
from members.forms import AddMemberForm
from payments.forms import AddPaymentForm


class ListMembers(LoginRequiredMixin, ListView):
    """List all members."""

    model = Member
    paginate_by = 50
    template_name = 'members/members.html'


class AddMember(LoginRequiredMixin, View):
    """Create a new member."""

    model = Member
    fields = '__all__'
    template_name = 'members/add.html'
    form_class = AddMemberForm
    success_url = reverse_lazy('member-list')
    member_prefix = 'member'
    payment_prefix = 'payment'

    def get_context_data(self):
        return {
            'member_form': AddMemberForm(self.request.POST or None,
                                         prefix=self.member_prefix),
            'payment_form': AddPaymentForm(self.request.POST or None,
                                         prefix=self.payment_prefix)
        }

    def get_response(self):
        return render(self.request,
                      self.template_name,
                      context=self.get_context_data())


    def get(self, request, *args, **kwargs):
        return self.get_response()

    def post(self, request, *args, **kwargs):
        member_form = AddMemberForm(request.POST,
                                    request.FILES,
                                    prefix=self.member_prefix)
        payment_form = AddPaymentForm(request.POST,
                                      prefix=self.payment_prefix)

        if member_form.is_valid() and payment_form.is_valid():
            member = member_form.save(commit=False)
            member.gym = self.request.user.gym
            member.save()
            payment = payment_form.save(commit=False)
            payment.user = member
            payment.save()
            return HttpResponseRedirect(self.success_url)
        else:
            return self.get_response()



class SendFeedbackView(LoginRequiredMixin, CreateView):  # pylint: disable=R0901
    """User send us feedback."""

    model = Feedback
    fields = ['text']
    success_url = reverse_lazy('thanks-feedback')
    template_name_suffix = '_create_form'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class FeedbackThanksView(LoginRequiredMixin, TemplateView):
    """Thanks user for sending us feedback."""

    template_name = 'members/feedback_thanks.html'
