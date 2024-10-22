# 2. Create a Booking, Delete the Booking with ID and Verify using GET request that it should not exist.

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

class Test_int_TC2:
    @allure.title("TC2 # Trying to GET details of Deleted Request")
    @allure.description(
        "TC#2 -> Create a Booking, Delete the Booking with ID and Verify using GET request that it should not exist.")
    @allure.tag("Integration", "p1")
    @allure.label("Tester", "Suresh")
    @allure.testcase("TC#2")
    @pytest.mark.Integration
    @pytest.mark.Negative
    def test_delete_req(self, create_token, get_booking_id):
        url = APIConstants().url_patch_put_delete(get_booking_id)
        print(url)
        headers = Utils().common_header_put_patch_delete_cookie(create_token)
        response = delete_requests(
            url=url,
            auth=None,
            headers=headers,
            in_json=False
        )
        verify_http_status_code(response, 201)
        verify_http_response_time(response, 200)

    def test_get_single_booking_id(self, get_booking_id):
        url = APIConstants().url_get_single_booking_with_id(get_booking_id)
        response = get_request(
            url=url,
            auth=None,
            in_json=False
        )
        verify_http_status_code(response, 404)



