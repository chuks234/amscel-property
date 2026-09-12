
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from cloudinary.models import CloudinaryField


class CompanyReview(models.Model):

    name = models.CharField(
        max_length=150
    )

    rating = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5),
        ]
    )

    comment = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Company Review"
        verbose_name_plural = "Company Reviews"

    def __str__(self):
        return f"{self.name} - {self.rating}/5"


class CompanyLeadership(models.Model):

    name = models.CharField(
        max_length=150
    )

    position = models.CharField(
        max_length=150
    )

    phone = models.CharField(
        max_length=30
    )

    email = models.EmailField()

    photo = CloudinaryField(
        "photo",
        folder="leadership"
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ["created_at"]
        verbose_name = "Company Leadership"
        verbose_name_plural = "Company Leadership"

    def __str__(self):
        return f"{self.name} - {self.position}"

