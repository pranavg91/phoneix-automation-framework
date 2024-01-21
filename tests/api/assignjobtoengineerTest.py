import sys
import requests

sys.path.append("C:/Users/Toto/Desktop/Phoenixautomationframework/")

def test_assignjob():
    base_url= "http://139.59.91.96:9000/v1/engineer/assign"

    headers={
        "Authorization":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiZmlyc3RfbmFtZSI6IkpvaG4iLCJsYXN0X25hbWUiOiJDZW5hIiwibG9naW5faWQiOiJpYW1zdXAiLCJtb2JpbGVfbnVtYmVyIjoiOTk4ODc3ODg5OSIsImVtYWlsX2lkIjoiam9obkBnbWFpbC5jb20iLCJwYXNzd29yZCI6IjVmNGRjYzNiNWFhNzY1ZDYxZDgzMjdkZWI4ODJjZjk5IiwicmVzZXRfcGFzc3dvcmRfZGF0ZSI6bnVsbCwibG9ja19zdGF0dXMiOjAsImlzX2FjdGl2ZSI6MSwibXN0X3JvbGVfaWQiOjIsIm1zdF9zZXJ2aWNlX2xvY2F0aW9uX2lkIjoxLCJjcmVhdGVkX2F0IjoiMjAyMS0xMS0wM1QwODowNjoyMy4wMDBaIiwibW9kaWZpZWRfYXQiOiIyMDIxLTEyLTIwVDA3OjQyOjAwLjAwMFoiLCJyb2xlX25hbWUiOiJTdXBlcnZpc29yIiwic2VydmljZV9sb2NhdGlvbiI6IlNlcnZpY2UgQ2VudGVyIEEiLCJpYXQiOjE2ODcxNDEyMDd9.3zocM1u_3qIDYZDKdX7GGhl6RvYEGjld1YlSi-cnxQg",  
        "Content-Type":"application/json"
}
    payload = {
        "job_id": 29108,
        "engineer_id":2
}

    response=requests.post(base_url,headers=headers,json = payload)
    print(response.status_code)
    assert response.status_code == 200
    assert "message" in response.text


   