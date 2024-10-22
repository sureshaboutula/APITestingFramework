# Full Update
import pytest
import allure
import requests
import logging
from src.helpers.api_requests_wrapper import *
from src.constants.api_constants import APIConstants
from src.helpers.payload_manager import *
from src.helpers.common_verification import *
from src.utils.utils import Utils

class Test_Full_Update_booking:

    def test_full_update_request(self, create_token):
        token = create_token
        booking_id = input("Enter booking_id : ")
        url = APIConstants().url_patch_put_delete(booking_id)
        headers = Utils().common_header_put_patch_delete_cookie(token)
        payload = payload_update_test()
        response = put_requests(
            url=url,
            auth=None,
            headers=headers,
            payload=payload,
            in_json=False
        )
        verify_http_status_code(response, 200)
        verify_http_response_time(response, 200)
        verify_response_key(response.json()["firstname"], "Jamesupdate")
        verify_response_key(response.json()["lastname"], "Brownupdate")
        verify_response_key(response.json()["bookingdates"]["checkin"], "2023-01-05")
