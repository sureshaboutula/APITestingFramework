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



