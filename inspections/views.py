from django.shortcuts import redirect, render

from .forms import InspectionForm


def book_inspection(request):

    property_id = request.GET.get("property")

    if request.method == "POST":

        form = InspectionForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("inspection_success")

    else:

        if property_id:
            form = InspectionForm(
                initial={"property": property_id}
            )
        else:
            form = InspectionForm()

    return render(
        request,
        "inspections/book_inspection.html",
        {"form": form}
    )


def inspection_success(request):

    return render(
        request,
        "inspections/inspection_success.html"
    )