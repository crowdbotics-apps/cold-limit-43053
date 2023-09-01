from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from nppes.utils import get_npi_details, check_npi_details


# Create your views here.
def verify_npi(request):
    npi_number = request.GET.get('number')
    if npi_number:
        result = get_npi_details(npi_number)
        details = check_npi_details(result)
        if details:
            return JsonResponse({"message": "success", "details": details})
    return JsonResponse({"message": "fail", "details": list()})
