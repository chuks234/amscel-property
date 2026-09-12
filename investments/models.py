from django.db import models


class InvestmentApplication(models.Model):

    name = models.CharField(max_length=150)

    phone = models.CharField(max_length=30)

    email = models.EmailField()

    investment_plan = models.CharField(max_length=150)

    address = models.TextField()

    next_of_kin = models.CharField(max_length=150)

    next_of_kin_phone = models.CharField(max_length=30)

    next_of_kin_address = models.TextField()

    amount = models.DecimalField(
        max_digits=15,
        decimal_places=2
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Investment Application"
        verbose_name_plural = "Investment Applications"

    def __str__(self):
        return f"{self.name} - {self.investment_plan}"