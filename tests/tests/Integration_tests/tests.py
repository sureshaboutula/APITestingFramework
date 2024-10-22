# 1. Verify that Create Booking -> Patch Request - Verify that firstName is updated.

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

class Test_int_TC1:
    @allure.title("TC1 # Trying to verify firstname on a Patch request")
    @allure.description("TC#1 -> Verify that Create Booking -> Patch Request - Verify that firstName is updated.")
    @allure.tag("Integration", "p1")
    @allure.label("Tester", "Suresh")
    @allure.testcase("TC#1")
    @pytest.mark.Integration

    def test_patch_req(self, create_token, get_booking_id):
        url = APIConstants().url_patch_put_delete(get_booking_id)
        # print(url)
        headers = Utils().common_header_put_patch_delete_cookie(create_token)
        payload = payload_patch_test()
        response = patch_requests(
            url=url,
            auth=None,
            headers=headers,
            payload=payload,
            in_json=False
        )

        resp_data = response.json()
        # print(response, resp_data)
        verify_http_status_code(response, 200)
        verify_http_response_time(response, 200)
        verify_response_key(resp_data["firstname"], "firsttest")
        verify_response_key(resp_data["lastname"], "lasttest")



# 2. Create a Booking, Delete the Booking with ID and Verify using GET request that it should not exist.
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


# 3. Get an Existing Booking id from Get All Bookings Ids , Update a Booking and Verify using GET by id.
class Test_int_TC3:
    @allure.title("TC3 # Trying to GET details of an Updated Request")
    @allure.description(
        "TC#2 -> Get an Existing Booking id from Get All Bookings Ids , Update a Booking and Verify using GET by id.")
    @allure.tag("Integration", "p1")
    @allure.label("Tester", "Suresh")
    @allure.testcase("TC#3")
    @pytest.mark.Integration
    def test_update_req(self,create_token, get_allbookings_req):
        booking_id = get_allbookings_req[125]["bookingid"]
        print(booking_id)
        url = APIConstants().url_patch_put_delete(booking_id)
        print(url)
        headers = Utils().common_header_put_patch_delete_cookie(create_token)
        print(headers)
        payload = payload_update_test()
        print(payload)
        response = put_requests(
            url=url,
            auth=None,
            headers=headers,
            payload=payload,
            in_json=False
        )
        print(response)
        verify_http_status_code(response, 200)
        verify_http_response_time(response, 200)

    def test_get_single_booking_id(self, get_allbookings_req):
        booking_id = get_allbookings_req[125]["bookingid"]
        url = APIConstants().url_get_single_booking_with_id(booking_id)
        response = get_request(
            url=url,
            auth=None,
            in_json=False
        )
        verify_http_status_code(response, 200)
        verify_response_key(response.json()["firstname"], "Jamesupdate")
        verify_response_key(response.json()["lastname"], "Brownupdate")