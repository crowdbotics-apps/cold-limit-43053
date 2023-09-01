import requests
import json

NPI_ENDPOINT = "https://npiregistry.cms.hhs.gov/api/?version=2.1"


def get_npi_details(number):
    url = f'{NPI_ENDPOINT}&number={number}'
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    return json.loads(response.text)


def check_npi_details(details):
    if "result_count" in details:
        if details["result_count"] > 0:
            return details["results"]



