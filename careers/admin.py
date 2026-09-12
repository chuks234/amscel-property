from django.contrib import admin

from .models import CareerApplication, CareerSetting, CareerPosition


@admin.register(CareerApplication)
class CareerApplicationAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "email",
        "phone",
        "created_at",
    )

    list_filter = (
        "created_at",
    )

    search_fields = (
        "name",
        "email",
        "phone",
        "address",
    )

    readonly_fields = (
        "created_at",
    )


@admin.register(CareerSetting)
class CareerSettingAdmin(admin.ModelAdmin):

    list_display = (
        "career_status",
        "updated_at",
    )

    readonly_fields = (
        "updated_at",
    )

    def career_status(self, obj):
        if obj.is_enabled:
            return "Enabled"
        return "Disabled"

    career_status.short_description = "Career Applications"

    def has_add_permission(self, request):
        return not CareerSetting.objects.exists()


@admin.register(CareerPosition)
class CareerPositionAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "department",
        "location",
        "employment_type",
        "application_deadline",
        "is_active",
        "created_at",
    )

    list_filter = (
        "is_active",
        "employment_type",
        "department",
        "created_at",
    )

    search_fields = (
        "title",
        "department",
        "location",
        "description",
        "requirements",
    )

    readonly_fields = (
        "created_at",
    )