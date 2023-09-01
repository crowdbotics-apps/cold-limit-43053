from django.urls import path

from nppes.views import (
   verify_npi
)

app_name = "nppes"
urlpatterns = [
    path("verify-npi/",verify_npi,name="verify-npi")
]
