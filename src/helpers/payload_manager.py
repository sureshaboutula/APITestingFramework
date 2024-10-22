
def payload_create_booking():
    payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2023-08-04",
            "checkout": "2023-08-11"
        },
        "additionalneeds": "Lunch"
    }
    return payload

def payload_create_token():
    payload = {
        "username": "admin",
        "password": "password123"
    }
    return payload

def payload_update_test():
    payload = {
        "firstname": "Jamesupdate",
        "lastname": "Brownupdate",
        "totalprice": 330,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2023-01-05",
            "checkout": "2023-02-01"
        },
        "additionalneeds": "Snacks"
    }
    return payload

def payload_patch_test():
    payload = {
        "firstname" : "firsttest",
        "lastname" : "lasttest"
    }
    return payload