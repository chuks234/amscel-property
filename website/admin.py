from django.contrib import admin

from .models import CompanyReview


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