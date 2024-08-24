import requests

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "hjkh34h3jk4hj34h3jh4",
    "username": "m5789hn",
    "agreeTermsOfService": "yes",  # Fixed typo here
    "notMinor": "yes",
}
    
response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)
