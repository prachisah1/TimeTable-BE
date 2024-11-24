from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("mainapp.urls")),
    path("mongo/", include('mainapp.mongo_driver_module.urls'))
]
