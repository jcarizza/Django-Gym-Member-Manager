from django.contrib import admin

from members.models import Feedback


class FeedbackAdmin(admin.ModelAdmin):
    """Model admin for feedback."""
    list_display = ('id', 'user', 'checked', 'on_date',)


admin.site.register(Feedback, FeedbackAdmin)
