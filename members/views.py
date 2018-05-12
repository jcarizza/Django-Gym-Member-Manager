"""Members views."""

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
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


class ListMembers(LoginRequiredMixin, ListView):
    """List all members."""

    model = Member
    paginate_by = 50
    template_name = 'members/members.html'


class AddMember(LoginRequiredMixin, FormView):
    """Create a new member."""

    model = Member
    fields = '__all__'
    template_name = 'members/add.html'
    form_class = AddMemberForm
    success_url = reverse_lazy('member-list')


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
