from django.db import models

from properties.models import Property


class Client(models.Model):
    PAYMENT_PLAN_CHOICES = [
        ("full", "Full Payment"),
        ("installment", "Instalment"),
    ]

    PAYMENT_STATUS_CHOICES = [
        ("pending", "Pending"),
        ("part_paid", "Part Paid"),
        ("paid", "Paid"),
    ]

    name = models.CharField(max_length=150)

    phone = models.CharField(max_length=30)

    email = models.EmailField(blank=True)

    address = models.TextField(blank=True)

    property = models.ForeignKey(
        Property,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="clients",
    )

    agreed_price = models.DecimalField(
        max_digits=15,
        decimal_places=2,
    )

    payment_plan = models.CharField(
        max_length=20,
        choices=PAYMENT_PLAN_CHOICES,
        default="full",
    )

    payment_status = models.CharField(
        max_length=20,
        choices=PAYMENT_STATUS_CHOICES,
        default="pending",
    )

    purchase_date = models.DateField(
        null=True,
        blank=True,
    )

    transaction_reference = models.CharField(
        max_length=100,
        blank=True,
    )

    notes = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Client Record"
        verbose_name_plural = "Client Records"

    def total_paid(self):
        return self.payments.aggregate(
            total=models.Sum("amount")
        )["total"] or 0

    def balance(self):
        return self.agreed_price - self.total_paid()

    def __str__(self):
        return self.name


class ClientPayment(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ("bank_transfer", "Bank Transfer"),
        ("cash", "Cash"),
        ("pos", "POS"),
        ("other", "Other"),
    ]

    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name="payments",
    )

    amount = models.DecimalField(
        max_digits=15,
        decimal_places=2,
    )

    payment_date = models.DateField()

    payment_method = models.CharField(
        max_length=30,
        choices=PAYMENT_METHOD_CHOICES,
    )

    reference = models.CharField(
        max_length=100,
        blank=True,
    )

    notes = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-payment_date", "-created_at"]
        verbose_name = "Client Payment"
        verbose_name_plural = "Client Payments"

    def __str__(self):
        return f"{self.client.name} - ₦{self.amount:,.2f}"