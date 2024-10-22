# Partial Update
import pytest
import allure
import requests
import logging
from src.helpers.api_requests_wrapper import *
from src.constants.api_constants import APIConstants
from src.helpers.payload_manager import *
from src.helpers.common_verification import *
from src.utils.utils import Utils

class Test_Partial_Update_booking:

    def test_partial_update_request(self, create_token):
        token = create_token
        booking_id = input("Enter booking_id : ")
        url = APIConstants().url_patch_put_delete(booking_id)
        headers = Utils().common_header_put_patch_delete_cookie(token)
        payload = payload_patch_test()
        print(url, headers, payload)
        response = patch_requests(
            url=url,
            auth=None,
            headers=headers,
            payload=payload,
            in_json=False
        )
        print(response)
        print(response.json())
        verify_http_status_code(response, 200)
        verify_http_response_time(response, 200)
        verify_response_key(response.json()["firstname"], "firsttest")
        verify_response_key(response.json()["lastname"], "lasttest")
