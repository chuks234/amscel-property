from django.contrib import admin
from .models import Property, PropertyImage, PropertyVideo


class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 3


class PropertyVideoInline(admin.TabularInline):
    model = PropertyVideo
    extra = 1


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "property_type",
        "location",
        "price",
        "plot_size",
        "status",
        "featured",
        "created_at",
    )

    list_filter = (
        "property_type",
        "status",
        "featured",
    )

    search_fields = (
        "title",
        "location",
        "description",
    )

    list_editable = (
        "status",
        "featured",
    )

    inlines = [
        PropertyImageInline,
        PropertyVideoInline,
    ]


@admin.register(PropertyImage)
class PropertyImageAdmin(admin.ModelAdmin):

    list_display = (
        "property",
        "caption",
        "uploaded_at",
    )


@admin.register(PropertyVideo)
class PropertyVideoAdmin(admin.ModelAdmin):

    list_display = (
        "property",
        "uploaded_at",
    )