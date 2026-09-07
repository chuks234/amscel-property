from django.urls import path

from . import views


urlpatterns = [
    path(
        "",
        views.book_inspection,
        name="book_inspection"
    ),

    path(
        "success/",
        views.inspection_success,
        name="inspection_success"
    ),
]
