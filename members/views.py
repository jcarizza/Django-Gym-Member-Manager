"""Members views."""

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    FormView,
)
from members.models import Member
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
