from django.contrib import admin
from .models import Mail


@admin.register(Mail)
class MailAdmin(admin.ModelAdmin):
    list_display = ("id", "subject", "sender", "receiver", "timestamp", "is_read")
    search_fields = ("subject", "sender__username", "receiver__username")
    list_filter = ("is_read", "timestamp")




