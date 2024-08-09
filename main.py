import os
from twilio.rest import Client
import requests


account_sid = "AC6a48448375ac7727f88d2463795f4a72"
auth_token = "71966dd76548905237e14d88ed995356"
api_key = "25879e0e5a66e9109483ba89a591d082"


parameters = {
    "lat": 28.971590,
    "lon": 77.696880,
    "appid": api_key,
    "cnt": 5

}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
data = response.json()
weather_id_list = []
id_at_6 = data["list"][0]['weather'][0]["id"]
weather_id_list.append(id_at_6)
id_at_9 = data["list"][1]['weather'][0]["id"]
weather_id_list.append(id_at_9)
id_at_12 = data["list"][2]['weather'][0]["id"]
weather_id_list.append(id_at_12)
id_at_15 = data["list"][3]['weather'][0]["id"]
weather_id_list.append(id_at_15)
id_at_18 = data["list"][4]['weather'][0]["id"]
weather_id_list.append(id_at_18)

for id in weather_id_list:
    if id < 700:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body="Its going to rain today you better bring an umbrella with you ☂️☂️☂️☂️",
            from_="+13218062309",
            to="+917906606858",
        )
        print(message.account_sid)
        break
