# Assuming MyAPIUtil is the module, and APIUtil is the class within that module
import sys
sys.path.append("C:/Users/Toto/Desktop/Phoenixautomationframework/")

from utils.APIUtil import APIUtil

headers = {
    # Your headers here
}

payload = {
    "username": "iamfd",
    "password": "password"
}

def test_login_api_request():
    # Assuming make_post_request is a method within the APIUtil class
    response = APIUtil.make_post_request("login", payload, headers)
    print(response.status_code)
    print(response.json())
    assert response.status_code == 200
    assert "Success" in response.text
    assert "message" in response.text

# Call the function to test the login API request
#test_login_api_request()