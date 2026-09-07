from django.shortcuts import render
from offices.models import Office
from properties.models import Property


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
    offices = Office.objects.filter(is_active=True)

    return render(
        request,
        "website/contact.html",
        {"offices": offices}
    )


def offices(request):
    offices = Office.objects.filter(is_active=True)

    return render(
        request,
        "website/offices.html",
        {"offices": offices}
    )


def houses(request):
    return render(request, "properties/house_list.html")