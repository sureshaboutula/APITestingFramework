
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


class TestGetAllBookingsRequest(object):

    @pytest.mark.get
    @pytest.mark.positive
    @allure.title("Test CRUD Operation GET")
    @allure.description("Varify that API receives all booking Ids with GET request")
    def test_get_all_bookings_request(self):
        url = APIConstants().url_get_booking()
        response = get_request(url=url, auth=None, in_json=False)
        response_data = response.json()
        verify_http_status_code(response_data=response, expected_data=200)
        verify_http_response_time(response=response, expected_data=200)




