"""Dashboard views."""

from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class DashboardView(LoginRequiredMixin, TemplateView):
    """Show dashboard."""
    template_name = 'dashboard.html'
