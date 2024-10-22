# Common Verification
 # HTTP Status Code
 # Headers
 # Data Verification
 # JSON Schema

def verify_http_status_code(response_data, expected_data):
    assert response_data.status_code == expected_data, "Failed ER != AR"

def verify_http_status_code_not_equal(response_data, expected_data):
    assert response_data.status_code != expected_data, "ER = AR"

def verify_http_response_time(response, expected_data):
    assert response.elapsed.total_seconds() <= expected_data, "Response is taking more than 200ms"
def verify_response_key(key, expected_data):
    assert key == expected_data

def verify_json_key_for_not_null(key):
    assert key != 0, "Failed - Key is not empty" + key
    assert key > 0, "Failed - Key is greater than zero"

def verify_json_key_for_not_null_token(key):
    assert key != 0, "Failed - Key is not empty" + key

def verify_response_key_should_not_be_none(key):
    assert key is not None

def verify_response_delete(response):
    assert "Created" in response