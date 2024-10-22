# Create Token
# Create Booking Id
# Update Booking(put) - Bookingid, token
# Delete the booking

import pytest
import allure
import requests
import logging
from src.helpers.api_requests_wrapper import *
from src.constants.api_constants import APIConstants
from src.helpers.payload_manager import *
from src.helpers.common_verification import *
from src.utils.utils import Utils

class TestCRUDBooking(object):
    @pytest.mark.positive
    @allure.title("Test CRUD Operation Update(PUT)")
    @allure.description("Varify that full update with the booking Id and token is working")
    def test_update_booking_id_token(self, create_token, get_booking_id):
        booking_id = get_booking_id
        token = create_token
        put_url = APIConstants().url_patch_put_delete(booking_id=booking_id)
        payload = payload_create_booking()
        payload["firstname"] = "Suresh"
        payload["lastname"] = "Ab"
        response = put_requests(
            url=put_url,
            auth=None,
            headers=Utils().common_header_put_patch_delete_cookie(token=token),
            payload=payload,
            in_json=False
        )
        verify_response_key(key=response.json()["firstname"], expected_data="Suresh")
        verify_response_key(key=response.json()["lastname"], expected_data="Ab")
        verify_http_status_code(response_data=response, expected_data=200)

    @allure.title("Test CRUD Operation Delete")
    @allure.description("Varify that Delete operation is working for the updated bookingid")
    def test_delete_booking_id(self, create_token, get_booking_id):
        booking_id = get_booking_id
        token = create_token
        delete_url = APIConstants().url_patch_put_delete(booking_id=booking_id)
        response  = delete_requests(
            url=delete_url,
            auth=None,
            headers=Utils().common_header_put_patch_delete_cookie(token=token),
            in_json=False
        )
        verify_response_delete(response=response.text)
        verify_http_status_code(response_data=response, expected_data=201)
