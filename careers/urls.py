from django.urls import path

from . import views


urlpatterns = [

    path(
        "",
        views.career,
        name="career"
    ),

    path(
        "success/",
        views.career_success,
        name="career_success"
    ),

]