from django.contrib import admin
from .models import Office


@admin.register(Office)
class OfficeAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "office_type",
        "city",
        "state",
        "phone",
        "is_active",
    )

    list_filter = (
        "office_type",
        "state",
        "is_active",
    )

    search_fields = (
        "name",
        "address",
        "city",
        "state",
    )