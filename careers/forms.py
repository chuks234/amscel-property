from django import forms

from .models import CareerApplication


class CareerApplicationForm(forms.ModelForm):

    class Meta:
        model = CareerApplication

        fields = [
            "name",
            "email",
            "phone",
            "address",
            "cv",
        ]

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "placeholder": "Your full name",
                }
            ),

            "email": forms.EmailInput(
                attrs={
                    "placeholder": "Your email address",
                }
            ),

            "phone": forms.TextInput(
                attrs={
                    "placeholder": "Your phone number",
                }
            ),

            "address": forms.Textarea(
                attrs={
                    "placeholder": "Your address",
                    "rows": 3,
                }
            ),

            "cv": forms.ClearableFileInput(
                attrs={
                    "accept": ".pdf,.doc,.docx",
                }
            ),
        }

    def clean_cv(self):
        cv = self.cleaned_data.get("cv")

        if cv:
            allowed_extensions = [
                ".pdf",
                ".doc",
                ".docx",
            ]

            extension = cv.name.lower().rsplit(".", 1)[-1]

            if f".{extension}" not in allowed_extensions:
                raise forms.ValidationError(
                    "Please upload your CV as a PDF, DOC, or DOCX file."
                )

        return cv