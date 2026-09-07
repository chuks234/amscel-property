from django.db import models


class Property(models.Model):
    PROPERTY_TYPES = [
        ("land", "Land"),
        ("house", "House"),
    ]

    STATUS_CHOICES = [
        ("available", "Available"),
        ("reserved", "Reserved"),
        ("sold", "Sold"),
    ]

    title = models.CharField(max_length=200)
    property_type = models.CharField(
        max_length=20,
        choices=PROPERTY_TYPES,
        default="land"
    )
    location = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    plot_size = models.CharField(max_length=100, blank=True)
    description = models.TextField()
    document_information = models.TextField(blank=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="available"
    )
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Property"
        verbose_name_plural = "Properties"


class PropertyImage(models.Model):
    property = models.ForeignKey(
        Property,
        on_delete=models.CASCADE,
        related_name="images"
    )
    image = models.ImageField(upload_to="properties/images/")
    caption = models.CharField(max_length=200, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image - {self.property.title}"

    class Meta:
        verbose_name = "Property Image"
        verbose_name_plural = "Property Images"


class PropertyVideo(models.Model):
    property = models.ForeignKey(
        Property,
        on_delete=models.CASCADE,
        related_name="videos"
    )
    video = models.FileField(upload_to="properties/videos/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Video - {self.property.title}"

    class Meta:
        verbose_name = "Property Video"
        verbose_name_plural = "Property Videos"
