from django.db import models
from properties.models import Property


class Inspection(models.Model):

    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("confirmed", "Confirmed"),
        ("completed", "Completed"),
        ("cancelled", "Cancelled"),
    ]

    property = models.ForeignKey(
        Property,
        on_delete=models.CASCADE
    )

    name = models.CharField(
        max_length=150
    )

    phone = models.CharField(
        max_length=30
    )

    email = models.EmailField(
        blank=True
    )

    inspection_date = models.DateField()

    inspection_time = models.TimeField()

    message = models.TextField(
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.name} - {self.property.title}"

    class Meta:
        ordering = ["inspection_date", "inspection_time"]