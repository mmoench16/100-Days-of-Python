import requests
import os
from dotenv import load_dotenv

load_dotenv()

pixela_endpoint = "https://pixe.la/v1/users"
pixela_api_token = os.getenv("PIXELA_API_TOKEN")


user_params = {
    "token": pixela_api_token,
    "username": "mmoench16",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)