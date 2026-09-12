
from django import forms

from .models import InvestmentApplication


class InvestmentApplicationForm(forms.ModelForm):

    class Meta:
        model = InvestmentApplication

        fields = [
            "name",
            "phone",
            "email",
            "investment_plan",
            "address",
            "next_of_kin",
            "next_of_kin_phone",
            "next_of_kin_address",
            "amount",
        ]

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "placeholder": "Your full name",
                }
            ),

            "phone": forms.TextInput(
                attrs={
                    "placeholder": "Your phone number",
                }
            ),

            "email": forms.EmailInput(
                attrs={
                    "placeholder": "Your email address",
                }
            ),

            "investment_plan": forms.Select(
                choices=[
                    ("6 months", "6 months"),
                    ("1 year", "1 year"),
                    ("2 years", "2 years"),
                    ("3 years", "3 years"),
                    ("More", "More"),
                ]
            ),

            "address": forms.Textarea(
                attrs={
                    "placeholder": "Your address",
                    "rows": 3,
                }
            ),

            "next_of_kin": forms.TextInput(
                attrs={
                    "placeholder": "Next of kin",
                }
            ),

            "next_of_kin_phone": forms.TextInput(
                attrs={
                    "placeholder": "Next of kin phone number",
                }
            ),

            "next_of_kin_address": forms.Textarea(
                attrs={
                    "placeholder": "Next of kin address",
                    "rows": 3,
                }
            ),

            "amount": forms.NumberInput(
                attrs={
                    "placeholder": "Investment amount",
                    "step": "0.01",
                }
            ),
        }

