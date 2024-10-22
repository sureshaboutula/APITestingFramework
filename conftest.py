
import pytest
import allure
import requests
import openpyxl
import random
from src.helpers.api_requests_wrapper import post_requests
from src.constants.api_constants import APIConstants
from src.helpers.payload_manager import *
from src.helpers.common_verification import *
from src.utils.utils import Utils

@pytest.fixture(scope="class")
def create_token():
    print("create_token fixture method is started")
    response = post_requests(
        url=APIConstants().url_create_token(),
        auth=None,
        headers=Utils().common_headers_json(),
        payload=payload_create_token(),
        in_json=False
    )
    verify_http_status_code(response_data=response, expected_data=200)
    verify_json_key_for_not_null_token(response.json()["token"])
    yield response.json()["token"]
    print("create_token fixture method is closed")

@pytest.fixture(scope="class")
def get_booking_id():
    print("get_booking_id fixture method is started")
    response = post_requests(
        url=APIConstants().url_create_booking(),
        auth=None,
        headers=Utils().common_headers_json(),
        payload=payload_create_booking(),
        in_json=False
    )
    booking_id = response.json()["bookingid"]
    verify_http_status_code(response_data=response, expected_data=200)
    verify_json_key_for_not_null(booking_id)
    yield booking_id
    print("get_booking_id fixture method is closed")

@pytest.fixture(scope="class")
def get_allbookings_req():
    print("get_allbookings_req fixture method is started")
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    Allurl = base_url + base_path
    response = requests.get(url=Allurl, verify=False)
    assert response.status_code == 200
    responseData = response.json()
    yield responseData
    print("get_allbookings_req fixture method is closed")


