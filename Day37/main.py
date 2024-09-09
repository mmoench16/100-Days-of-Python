import requests
import os
from dotenv import load_dotenv

load_dotenv()

USERNAME = "mmoench16"

pixela_endpoint = "https://pixe.la/v1/users"
pixela_api_token = os.getenv("PIXELA_API_TOKEN")


user_params = {
    "token": pixela_api_token,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# graph_config = {
#     "id": "graph1",
#     "name": "Cycling Graph",
#     "unit": "km",
#     "type": "float",
#     "color": "sora"
# }

headers = {
    "X-USER-TOKEN": pixela_api_token
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_config = {
    "date": "20240909",
    "quantity": "25.2"
}

pixel_endpoint = f"{graph_endpoint}/graph1"

response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)