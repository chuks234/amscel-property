from django.contrib import admin
from .models import Inspection


@admin.register(Inspection)
class InspectionAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "property",
        "inspection_date",
        "inspection_time",
        "status",
    )

    list_filter = (
        "status",
        "inspection_date",
    )

    search_fields = (
        "name",
        "phone",
        "email",
    )