import sys
sys.path.append("C:/Users/Toto/Desktop/Phoenixautomationframework/")

from utils.APIUtil import APIUtil

payload={
"username":"iamsup",
"password":"password"
}
headers={

}
def test_SUP_login():
    response=APIUtil.make_post_request("login",payload,headers)
    response.status_code == 200  
    assert "data" in response.json()
    assert "Success" in response.json()