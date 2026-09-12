from django.urls import path

from . import views


urlpatterns = [

    path(
        "",
        views.investment,
        name="investment"
    ),

    path(
        "success/",
        views.investment_success,
        name="investment_success"
    ),

]