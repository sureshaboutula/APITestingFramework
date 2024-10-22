import pytest
import allure
import requests
import logging
from src.helpers.api_requests_wrapper import *
from src.constants.api_constants import APIConstants
from src.helpers.payload_manager import *
from src.helpers.common_verification import *
from src.utils.utils import Utils

class Test_Get_Booking:
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    def test_get_booking(self):
        booking_id = input("Enter booking_id : ")
        url = APIConstants().url_get_single_booking()+booking_id
        print(url)
        try:
            response = get_booking(
                url=url,
                auth=None
            )
        except Exception as e:
            logging.error("Error fetching booking: %s", e)
            return e
        else:
            verify_http_status_code(response, 200)
            verify_http_response_time(response, 200)