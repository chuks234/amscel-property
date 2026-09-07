from django.contrib import admin
from .models import Enquiry


@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "phone",
        "property",
        "created_at",
    )

    search_fields = (
        "name",
        "phone",
        "email",
    )

    list_filter = (
        "created_at",
    )