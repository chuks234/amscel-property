from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


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