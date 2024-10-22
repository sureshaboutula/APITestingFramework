# 5. Invalid Creation - enter a wrong payload or Wrong JSON.

import pytest
import allure
import requests
import logging
import json
from src.helpers.api_requests_wrapper import *
from src.constants.api_constants import APIConstants
from src.helpers.payload_manager import *
from src.helpers.common_verification import *
from src.utils.utils import Utils

class Test_int_TC5:
    @allure.title("TC5 # Trying to Verify Create a booking with Invalid or empty payload")
    @allure.description("TC#5 -> Invalid Creation - enter a wrong payload or Wrong JSON.")
    @allure.tag("Integration", "p1")
    @allure.label("Tester", "Suresh")
    @allure.testcase("TC#5")
    @pytest.mark.Integration
    @pytest.mark.Negative
    def test_create_booking_id_emptypayload(self):
        url = APIConstants().url_create_booking()
        headers = Utils().common_headers_json()
        response = post_requests(
            url=url,
            auth=None,
            headers=headers,
            payload={},
            in_json=False
        )
        verify_http_status_code(response, 500)

    def test_create_booking_id_invalidheader(self):
        url = APIConstants().url_create_booking()
        headers = Utils().common_headers_xml()
        payload = payload_create_booking()
        response = post_requests(
            url=url,
            auth=None,
            headers=headers,
            payload={},
            in_json=False
        )
        verify_http_status_code(response, 400)

    def test_create_booking_id_invalidpayload(self):
        url = APIConstants().url_create_booking()
        headers = Utils().common_headers_json()
        payload = {
            "firstname": "Jim",
            "totalprice": 111,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2023-08-04",
                "checkout": "2023-08-11"
            },
            "additionalneeds": "Lunch"
        }
        response = post_requests(
            url=url,
            auth=None,
            headers=headers,
            payload=payload,
            in_json=False
        )
        verify_http_status_code_not_equal(response, 200)