import sys
import requests
sys.path.append("C:/Users/Toto/Desktop/Phoenixautomationframework")

def test_qccomplete():

    base= "http://139.59.91.96:9000/v1/qc"

    headers={
        "Authorization":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MywiZmlyc3RfbmFtZSI6InFjIiwibGFzdF9uYW1lIjoicWMiLCJsb2dpbl9pZCI6ImlhbXFjIiwibW9iaWxlX251bWJlciI6Ijg4OTk3NzY2NTUiLCJlbWFpbF9pZCI6Im1hcmtAZ21haWwuY29tIiwicGFzc3dvcmQiOiI1ZjRkY2MzYjVhYTc2NWQ2MWQ4MzI3ZGViODgyY2Y5OSIsInJlc2V0X3Bhc3N3b3JkX2RhdGUiOm51bGwsImxvY2tfc3RhdHVzIjowLCJpc19hY3RpdmUiOjEsIm1zdF9yb2xlX2lkIjo0LCJtc3Rfc2VydmljZV9sb2NhdGlvbl9pZCI6MSwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDNUMDg6MDY6MjMuMDAwWiIsIm1vZGlmaWVkX2F0IjoiMjAyMS0xMS0wM1QwODowNjoyMy4wMDBaIiwicm9sZV9uYW1lIjoiUUMiLCJzZXJ2aWNlX2xvY2F0aW9uIjoiU2VydmljZSBDZW50ZXIgQSIsImlhdCI6MTY4NzE0MTY3Mn0.nXaGN5fJxf6DRJk1K4HvXEKq-BiroaJ8i_mSXins5jA",  
        "Content-Type":"application/json"
        }
    payload={
        "job_id":25388
        }
   
    response=requests.post(base,headers=headers,json=payload)
    print(response.status_code)
    assert response.status_code == 403
    

