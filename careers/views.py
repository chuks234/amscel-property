
from django.shortcuts import render, redirect

from .forms import CareerApplicationForm
from .models import CareerSetting, CareerPosition


def career(request):

    career_setting, created = CareerSetting.objects.get_or_create(
        pk=1,
        defaults={
            "is_enabled": True
        }
    )

    positions = CareerPosition.objects.filter(
        is_active=True
    )

    if not career_setting.is_enabled:
        return render(
            request,
            "career_closed.html",
            {
                "positions": positions
            }
        )

    if request.method == "POST":

        form = CareerApplicationForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            return redirect("career_success")

    else:

        form = CareerApplicationForm()

    return render(
        request,
        "career.html",
        {
            "form": form,
            "positions": positions
        }
    )


def career_success(request):

    return render(
        request,
        "career_success.html"
    )

