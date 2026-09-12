
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import CompanyReview


class CustomerRegistrationForm(UserCreationForm):

    first_name = forms.CharField(
        max_length=150,
        required=True
    )

    last_name = forms.CharField(
        max_length=150,
        required=True
    )

    email = forms.EmailField(
        required=True
    )

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        )

    def clean_email(self):
        email = self.cleaned_data["email"]

        if User.objects.filter(
            email__iexact=email
        ).exists():
            raise forms.ValidationError(
                "An account with this email already exists."
            )

        return email


class CompanyReviewForm(forms.ModelForm):

    class Meta:
        model = CompanyReview

        fields = (
            "rating",
            "comment",
        )

        widgets = {
            "rating": forms.Select(
                choices=[
                    (5, "★★★★★ 5 - Excellent"),
                    (4, "★★★★☆ 4 - Very Good"),
                    (3, "★★★☆☆ 3 - Good"),
                    (2, "★★☆☆☆ 2 - Fair"),
                    (1, "★☆☆☆☆ 1 - Poor"),
                ]
            ),

            "comment": forms.Textarea(
                attrs={
                    "rows": 4,
                    "placeholder": (
                        "Share your experience with AMSCEL Property Limited..."
                    )
                }
            ),
        }

