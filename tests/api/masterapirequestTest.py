import sys
sys.path.append("C:/Users/Toto/Desktop/Phoenixautomationframework/")

from utils.APIUtil import APIUtil

headers ={
    "Authorization":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MiwiZmlyc3RfbmFtZSI6Ik1hcmsiLCJsYXN0X25hbWUiOiJ6dWsiLCJsb2dpbl9pZCI6ImlhbWVuZyIsIm1vYmlsZV9udW1iZXIiOiI4ODk5Nzc2NjU1IiwiZW1haWxfaWQiOiJtYXJrQGdtYWlsLmNvbSIsInBhc3N3b3JkIjoiNWY0ZGNjM2I1YWE3NjVkNjFkODMyN2RlYjg4MmNmOTkiLCJyZXNldF9wYXNzd29yZF9kYXRlIjpudWxsLCJsb2NrX3N0YXR1cyI6MCwiaXNfYWN0aXZlIjoxLCJtc3Rfcm9sZV9pZCI6MSwibXN0X3NlcnZpY2VfbG9jYXRpb25faWQiOjEsImNyZWF0ZWRfYXQiOiIyMDIxLTExLTAzVDA4OjA2OjIzLjAwMFoiLCJtb2RpZmllZF9hdCI6IjIwMjEtMTItMjBUMDc6NDI6MDAuMDAwWiIsInJvbGVfbmFtZSI6IkVuZ2luZWVyIiwic2VydmljZV9sb2NhdGlvbiI6IlNlcnZpY2UgQ2VudGVyIEEiLCJpYXQiOjE2ODcxNDE1MDd9.TjQKobMwE_Aelzc9gKH2JZaRwpmeTRFN5TeOgKtWmjg"
}
payload ={

}

def test_mastererquest():
    response=APIUtil.make_post_request("/master",payload, headers)
    print(response.json())
    assert response.status_code == 200