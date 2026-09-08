from django.shortcuts import render, redirect

from offices.models import Office
from properties.models import Property
from enquiries.models import Enquiry


def home(request):
    properties = Property.objects.filter(
        property_type="land",
        status="available",
        featured=True
    )[:6]

    return render(
        request,
        "website/home.html",
        {"properties": properties}
    )


def about(request):
    return render(request, "website/about.html")


def contact(request):
    if request.method == "POST":
        Enquiry.objects.create(
            name=request.POST.get("name"),
            phone=request.POST.get("phone"),
            email=request.POST.get("email"),
            message=request.POST.get("message"),
        )

        return redirect("contact_success")

    return render(request, "website/contact.html")


def contact_success(request):
    return render(request, "website/contact_success.html")


def offices(request):
    offices = Office.objects.filter(is_active=True)

    return render(
        request,
        "website/offices.html",
        {"offices": offices}
    )


def houses(request):
    return render(request, "properties/house_list.html")