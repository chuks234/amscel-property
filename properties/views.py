from django.shortcuts import get_object_or_404, render

from .models import Property


def land_list(request):
    properties = Property.objects.filter(
        property_type="land",
        status="available"
    )

    return render(
        request,
        "properties/land_list.html",
        {"properties": properties}
    )


def property_detail(request, pk):
    property = get_object_or_404(Property, pk=pk)

    return render(
        request,
        "properties/property_detail.html",
        {"property": property}
    )
