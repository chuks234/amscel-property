from django.db import models


class Office(models.Model):

    OFFICE_TYPES = [
        ("head", "Head Office"),
        ("branch", "Branch Office"),
    ]

    name = models.CharField(max_length=200)

    office_type = models.CharField(
        max_length=20,
        choices=OFFICE_TYPES,
        default="branch"
    )

    address = models.TextField()

    city = models.CharField(
        max_length=100,
        default="Abuja"
    )

    state = models.CharField(
        max_length=100,
        default="FCT"
    )

    phone = models.CharField(
        max_length=30,
        blank=True
    )

    whatsapp = models.CharField(
        max_length=30,
        blank=True
    )

    email = models.EmailField(
        blank=True
    )

    opening_hours = models.CharField(
        max_length=255,
        blank=True
    )

    google_maps_url = models.URLField(
        blank=True
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["office_type", "name"]