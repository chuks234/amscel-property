from django import forms

from .models import CompanyReview


class CompanyReviewForm(forms.ModelForm):

    class Meta:
        model = CompanyReview
        fields = [
            "name",
            "rating",
            "comment",
        ]

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "placeholder": "Your name",
                }
            ),

            "rating": forms.Select(
                choices=[
                    (5, "★★★★★ Excellent"),
                    (4, "★★★★ Very Good"),
                    (3, "★★★ Good"),
                    (2, "★★ Fair"),
                    (1, "★ Poor"),
                ]
            ),

            "comment": forms.Textarea(
                attrs={
                    "placeholder": "Tell us about your experience with AMSCEL Property Limited",
                    "rows": 4,
                }
            ),
        }