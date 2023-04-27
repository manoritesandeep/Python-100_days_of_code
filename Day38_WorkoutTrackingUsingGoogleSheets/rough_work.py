# import requests
#
# sheety_api_key = ""
#
# sheety_get_endpoint = "https://api.sheety.co/3e86ff5cf468163f0e79d65eff837b5d/myWorkouts/workouts"
#
# # response = requests.get(url=sheety_get_endpoint)
# # print(response.json())
#
# sheety_post_endpoint = "https://api.sheety.co/3e86ff5cf468163f0e79d65eff837b5d/myWorkouts/workouts"
#
# # response = requests.post(url=sheety_get_endpoint)
# # print(response.json())
#

from datetime import datetime
today = datetime.now().strftime("%d%m%Y")
current_time = datetime.now().strftime("%X")
print(today, current_time)




