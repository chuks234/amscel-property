from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", include("website.urls")),

    path("", include("properties.urls")),

    path(
        "inspections/",
        include("inspections.urls")
    ),

    path(
        "account/",
        include("accounts.urls")
    ),

    path(
        "investment/",
        include("investments.urls")
    ),
    
    path(
        "career/",
        include("careers.urls")
    ),
   
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )