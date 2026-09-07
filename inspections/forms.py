from django import forms

from .models import Inspection


class InspectionForm(forms.ModelForm):

    class Meta:
        model = Inspection

        fields = [
            "property",
            "name",
            "phone",
            "email",
            "inspection_date",
            "inspection_time",
            "message",
        ]

        widgets = {
            "inspection_date": forms.DateInput(
                attrs={"type": "date"}
            ),
            "inspection_time": forms.TimeInput(
                attrs={"type": "time"}
            ),
            "message": forms.Textarea(
                attrs={
                    "placeholder": "Any additional information?"
                }
            ),
        }
