import requests
import os
from datetime import datetime
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

today = datetime.now().strftime("%Y%m%d")

pixel_config = {
    "date": today,
    "quantity": "45.3"
}

pixel_update_config = {
    "quantity": "45.3"
}

pixel_endpoint = f"{graph_endpoint}/graph1"
pixel_update_endpoint = f"{graph_endpoint}/graph1/{today}"
pixel_delete_endpoint = f"{graph_endpoint}/graph1/{today}"


# response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
# response = requests.put(url=pixel_update_endpoint, json=pixel_update_config, headers=headers)
response = requests.delete(url=pixel_delete_endpoint, headers=headers)
print(response.text)