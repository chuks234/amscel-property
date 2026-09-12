from django.shortcuts import render, redirect

from .forms import InvestmentApplicationForm


def investment(request):

    if request.method == "POST":

        form = InvestmentApplicationForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("investment_success")

    else:

        form = InvestmentApplicationForm()

    return render(
        request,
        "investment.html",
        {"form": form}
    )


def investment_success(request):

    return render(
        request,
        "investment_success.html"
    )