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

class TestDeleteBooking:

    def test_delete_booking(self, create_token):
        token = create_token
        booking_id = input("Enter booking_id : ")
        url = APIConstants().url_patch_put_delete(booking_id)
        headers = Utils().common_header_put_patch_delete_cookie(token)
        response = delete_requests(
            url=url,
            auth=None,
            headers=headers,
            in_json=False
        )
        verify_http_status_code(response, 201)
        verify_http_response_time(response, 200)