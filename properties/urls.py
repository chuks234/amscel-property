from django.urls import path

from . import views

urlpatterns = [
    path("land/", views.land_list, name="land_list"),
    path(
        "property/<int:pk>/",
        views.property_detail,
        name="property_detail"
    ),
]
