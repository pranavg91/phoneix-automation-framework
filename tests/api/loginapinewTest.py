import sys
import requests
sys.path.append("C:/Users/Toto/Desktop/Phoenixautomationframework/")

from utils.APIlogin import APIlogin

headers ={
}
payload ={

    "username":"iamfd",
    "password":"password"
}

def test_login_form():
    response=APIlogin.make_post_request("login",payload,headers)
    print(response.json())
    assert response.status_code == 200