
import pytest
import allure
import requests
import logging
from src.helpers.api_requests_wrapper import *
from src.constants.api_constants import APIConstants
from src.helpers.payload_manager import *
from src.helpers.common_verification import *
from src.utils.utils import Utils

class TestPingRequest(object):

    @pytest.mark.health
    @allure.title("Test CRUD Operation Update(PUT)")
    @allure.description("Varify that full update with the booking Id and token is working")
    def test_ping_request(self):
        response = ping_request(
            url=APIConstants().base_url(),
            auth=None,
            headers=None
        )
        verify_http_status_code(response_data=response, expected_data=200)
        verify_http_response_time(response.elapsed.total_seconds(), 200)
