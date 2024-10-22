# APIConstants - Class which will contain all the endpoints
# Keep the URLs

class APIConstants(object):

    def base_url(self):
        return "https://restful-booker.herokuapp.com/"

    def url_create_booking(self):
        return "https://restful-booker.herokuapp.com/booking"

    def url_get_booking(self):
        return "https://restful-booker.herokuapp.com/booking"

    def url_get_single_booking(self):
        return "https://restful-booker.herokuapp.com/booking/"

    def url_get_single_booking_with_id(self, booking_id):
        return "https://restful-booker.herokuapp.com/booking/" + str(booking_id)

    def url_create_token(self):
        return "https://restful-booker.herokuapp.com/auth"

    # Update, Patch, put and delete URL
    def url_patch_put_delete(self, booking_id):
        return "https://restful-booker.herokuapp.com/booking/" + str(booking_id)