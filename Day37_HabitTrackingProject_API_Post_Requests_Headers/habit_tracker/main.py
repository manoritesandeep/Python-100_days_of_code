import requests
from datetime import datetime

TOKEN = "jkasdlkjfal565s"
USERNAME = "sandeepsolanki"
# check graph @ https://pixe.la/v1/users/sandeepsolanki/graphs/graph1.html
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint,
#                          json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Cycling graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint,
#                          json=graph_config,
#                          headers=headers)
# print(response.text)

today = datetime.now()
# print(today.strftime("%Y%m%d"))

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}"

pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many Kms did you cycle today? "),
}

response = requests.post(url=pixel_endpoint,
                         json=pixel_config,
                         headers=headers)
print(response.text)

update_date = today.strftime("%Y%m%d")
update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}/{update_date}"

update_config = {
    "quantity": "15",
}

# response = requests.put(url=update_pixel_endpoint,
#                         json=update_config,
#                         headers=headers)
# print(response.text)

delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}/{today.strftime('%Y%m%d')}"

# response = requests.delete(url=delete_pixel_endpoint,
#                            headers=headers)
# print(response.text)
