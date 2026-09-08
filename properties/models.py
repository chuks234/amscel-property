from io import BytesIO

from django.core.files.base import ContentFile
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from django.db import models
from PIL import Image


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

    image = models.ImageField(
        upload_to="properties/images/"
    )

    caption = models.CharField(
        max_length=200,
        blank=True
    )

    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )

    def save(self, *args, **kwargs):
        if self.image:
            try:
                img = Image.open(self.image)

                # Convert images with transparency to RGB safely
                if img.mode in ("RGBA", "LA", "P"):
                    background = Image.new(
                        "RGB",
                        img.size,
                        "white"
                    )

                    if img.mode == "P":
                        img = img.convert("RGBA")

                    background.paste(
                        img,
                        mask=img.getchannel("A")
                        if img.mode == "RGBA"
                        else None
                    )

                    img = background

                else:
                    img = img.convert("RGB")

                # Maximum image size
                max_width = 1600
                max_height = 1200

                img.thumbnail(
                    (max_width, max_height),
                    Image.Resampling.LANCZOS
                )

                # Save compressed JPEG
                output = BytesIO()

                img.save(
                    output,
                    format="JPEG",
                    quality=82,
                    optimize=True
                )

                output.seek(0)

                # Always save the processed image as .jpg
                filename = self.image.name.rsplit("/", 1)[-1]
                filename = filename.rsplit(".", 1)[0] + ".jpg"

                self.image.save(
                    filename,
                    ContentFile(output.read()),
                    save=False
                )

            except Exception as e:
                raise ValidationError(
                    f"Unable to process the uploaded image: {e}"
                )

        super().save(*args, **kwargs)

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

    video = models.FileField(
        upload_to="properties/videos/",
        validators=[
            FileExtensionValidator(
                allowed_extensions=["mp4", "webm", "mov"],
                message="Please upload a valid video file (MP4, WebM, or MOV)."
            )
        ]
    )

    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )

    def clean(self):
        super().clean()

        if self.video:
            max_size = 50 * 1024 * 1024  # 50 MB

            if self.video.size > max_size:
                raise ValidationError(
                    "Video file is too large. "
                    "Please upload a video smaller than 50 MB."
                )

    def __str__(self):
        return f"Video - {self.property.title}"

    class Meta:
        verbose_name = "Property Video"
        verbose_name_plural = "Property Videos"