# 4. Create a BOOKING, Delete It

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

class Test_int_TC4:
    @allure.title("TC4 # Trying to Delete a newly created booking")
    @allure.description("TC#4 -> Verify Delete Request on a Created Booking")
    @allure.tag("Integration", "p1")
    @allure.label("Tester", "Suresh")
    @allure.testcase("TC#4")
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


