import requests

class APIlogin:
    BASE_URL = "http://139.59.91.96:9000/v1/"

    def __init__(self):
        print("APIlogin")

    @staticmethod 
    def make_get_request(endpoint, headers):
        response = requests.get(APIlogin.BASE_URL+endpoint, headers = headers)
        return response

    @staticmethod 
    def make_post_request(endpoint, payload, headers):
       response =  requests.post(APIlogin.BASE_URL+endpoint, data=payload, headers=headers)
       return response