import requests

def apiCall(param):
    res = requests.get(f"https://localhost/api?param={param}")
    if(res.status_code == 200):
        return res.json()
    else:
        raise ValueError("API call failed")