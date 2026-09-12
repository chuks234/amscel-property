
from django.db import models


class CareerApplication(models.Model):

    name = models.CharField(max_length=150)

    email = models.EmailField()

    phone = models.CharField(max_length=30)

    address = models.TextField()

    cv = models.FileField(upload_to="career_cvs/")

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Career Application"
        verbose_name_plural = "Career Applications"

    def __str__(self):
        return self.name


class CareerSetting(models.Model):

    is_enabled = models.BooleanField(
        default=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = "Career Setting"
        verbose_name_plural = "Career Settings"

    def __str__(self):
        return "Career Application Settings"


class CareerPosition(models.Model):

    title = models.CharField(
        max_length=150
    )

    department = models.CharField(
        max_length=150,
        blank=True
    )

    location = models.CharField(
        max_length=150,
        default="Abuja, Nigeria"
    )

    employment_type = models.CharField(
        max_length=100,
        default="Full-time"
    )

    description = models.TextField()

    requirements = models.TextField()

    application_deadline = models.DateField(
        null=True,
        blank=True
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Career Position"
        verbose_name_plural = "Career Positions"

    def __str__(self):
        return self.title

