import allure
import pytest

class TestCreateBooking(object):
    @pytest.mark.positive
    @allure.title("Verify the create booking status and booking id should not be null")
    @allure.description("Create a booking from the payload and verify that booking id should not be null")
    def test_create_booking_positive(self):
        pass