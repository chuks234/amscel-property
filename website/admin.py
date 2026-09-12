
from django.contrib import admin

from .models import CompanyReview, CompanyLeadership


@admin.register(CompanyReview)
class CompanyReviewAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "rating",
        "comment",
        "created_at",
    )

    list_filter = (
        "rating",
        "created_at",
    )

    search_fields = (
        "name",
        "comment",
    )

    readonly_fields = (
        "created_at",
    )


@admin.register(CompanyLeadership)
class CompanyLeadershipAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "position",
        "phone",
        "email",
        "is_active",
        "created_at",
    )

    list_filter = (
        "is_active",
        "position",
        "created_at",
    )

    search_fields = (
        "name",
        "position",
        "phone",
        "email",
    )

    readonly_fields = (
        "created_at",
    )

