# 6. Trying to Update on a Delete Id -> 405

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

class Test_int_TC6:
    @allure.title("TC6 # Trying to Update on a Delete Id")
    @allure.description("TC#6 -> Verify PUT Request on a Deleted Id")
    @allure.tag("Integration", "p1")
    @allure.label("Tester", "Suresh")
    @allure.testcase("TC#6")
    @pytest.mark.Integration

    def test_delete_req(self,create_token, get_booking_id):
        print(create_token)
        print(get_booking_id)
        url = APIConstants().url_patch_put_delete(get_booking_id)
        headers = Utils().common_header_put_patch_delete_cookie(create_token)
        response = delete_requests(
            url=url,
            auth=None,
            headers=headers,
            in_json=False
        )
        print(response)
        verify_http_status_code(response, 201)
        verify_http_response_time(response, 200)

    def test_update_req(self,create_token, get_booking_id):
        url = APIConstants().url_patch_put_delete(get_booking_id)
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
        verify_http_status_code(response, 405)
        verify_http_response_time(response, 200)



