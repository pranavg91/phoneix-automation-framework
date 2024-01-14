import sys

sys.path.append("C:/Users/Toto/Desktop/Phoenixautomationframework/")

from utils.APIUtil import APIUtil

headers ={
 }

payload={
    "username" : "iameng",
    "password":  "password"
}

def test_login_engineer_user():
    response = APIUtil.make_post_request("login", payload, headers)
    print(response.status_code)
