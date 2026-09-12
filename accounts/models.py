from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class CompanyReview(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="company_reviews"
    )

    rating = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5),
        ]
    )

    comment = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

        constraints = [
            models.UniqueConstraint(
                fields=["user"],
                name="unique_user_company_review"
            )
        ]

    def __str__(self):
        return (
            f"{self.user.username} - "
            f"AMSCEL Property Limited - "
            f"{self.rating}/5"
        )