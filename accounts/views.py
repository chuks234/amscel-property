
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CompanyReviewForm, CustomerRegistrationForm
from .models import CompanyReview


def register(request):

    if request.user.is_authenticated:
        return redirect("accounts:dashboard")

    if request.method == "POST":
        form = CustomerRegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            messages.success(
                request,
                "Your account has been created successfully."
            )

            return redirect("accounts:dashboard")

    else:
        form = CustomerRegistrationForm()

    return render(
        request,
        "accounts/register.html",
        {
            "form": form,
        }
    )


@login_required
def dashboard(request):

    review = CompanyReview.objects.filter(
        user=request.user
    ).first()

    return render(
        request,
        "accounts/dashboard.html",
        {
            "review": review,
        }
    )


@login_required
def add_review(request):

    existing_review = CompanyReview.objects.filter(
        user=request.user
    ).first()

    if request.method == "POST":

        if existing_review:
            form = CompanyReviewForm(
                request.POST,
                instance=existing_review
            )
        else:
            form = CompanyReviewForm(request.POST)

        if form.is_valid():

            review = form.save(commit=False)

            review.user = request.user

            review.save()

            messages.success(
                request,
                "Your review has been submitted successfully."
            )

            return redirect("accounts:dashboard")

    else:

        if existing_review:
            form = CompanyReviewForm(
                instance=existing_review
            )
        else:
            form = CompanyReviewForm()

    return render(
        request,
        "accounts/review.html",
        {
            "form": form,
            "existing_review": existing_review,
        }
    )


@login_required
def delete_review(request, review_id):

    review = get_object_or_404(
        CompanyReview,
        id=review_id,
        user=request.user
    )

    if request.method == "POST":
        review.delete()

        messages.success(
            request,
            "Your review has been deleted."
        )

    return redirect("accounts:dashboard")

