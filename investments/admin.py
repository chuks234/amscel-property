from django.contrib import admin

from .models import InvestmentApplication


@admin.register(InvestmentApplication)
class InvestmentApplicationAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "phone",
        "email",
        "investment_plan",
        "amount",
        "created_at",
    )

    list_filter = (
        "investment_plan",
        "created_at",
    )

    search_fields = (
        "name",
        "phone",
        "email",
        "investment_plan",
        "next_of_kin",
    )

    readonly_fields = (
        "created_at",
    )