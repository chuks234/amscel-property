from django.contrib import admin
import csv

from django.http import HttpResponse

from .models import Client, ClientPayment


class ClientPaymentInline(admin.TabularInline):
    model = ClientPayment
    extra = 1

    fields = (
        "amount",
        "payment_date",
        "payment_method",
        "reference",
        "notes",
    )


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "phone",
        "property",
        "agreed_price",
        "payment_plan",
        "payment_status",
        "total_paid_display",
        "balance_display",
        "purchase_date",
    )

    list_filter = (
        "payment_plan",
        "payment_status",
        "purchase_date",
    )

    search_fields = (
        "name",
        "phone",
        "email",
        "transaction_reference",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    inlines = [
        ClientPaymentInline,
    ]

    actions = [
        "export_clients_csv",
    ]

    def total_paid_display(self, obj):
        return f"₦{obj.total_paid():,.2f}"

    total_paid_display.short_description = "Total Paid"

    def balance_display(self, obj):
        return f"₦{obj.balance():,.2f}"

    balance_display.short_description = "Balance"

    @admin.action(description="Download selected clients as CSV")
    def export_clients_csv(self, request, queryset):
        response = HttpResponse(
            content_type="text/csv"
        )

        response["Content-Disposition"] = (
            'attachment; filename="client_records.csv"'
        )

        writer = csv.writer(response)

        writer.writerow([
            "Client Name",
            "Phone",
            "Email",
            "Address",
            "Property",
            "Property Type",
            "Agreed Price",
            "Payment Plan",
            "Payment Status",
            "Total Paid",
            "Balance",
            "Purchase Date",
            "Transaction Reference",
            "Notes",
        ])

        for client in queryset:
            property_name = ""
            property_type = ""

            if client.property:
                property_name = client.property.title
                property_type = client.property.property_type

            writer.writerow([
                client.name,
                client.phone,
                client.email,
                client.address,
                property_name,
                property_type,
                client.agreed_price,
                client.get_payment_plan_display(),
                client.get_payment_status_display(),
                client.total_paid(),
                client.balance(),
                client.purchase_date,
                client.transaction_reference,
                client.notes,
            ])

        return response


@admin.register(ClientPayment)
class ClientPaymentAdmin(admin.ModelAdmin):
    list_display = (
        "client",
        "amount",
        "payment_date",
        "payment_method",
        "reference",
    )

    list_filter = (
        "payment_method",
        "payment_date",
    )

    search_fields = (
        "client__name",
        "client__phone",
        "reference",
    )

    readonly_fields = (
        "created_at",
    )