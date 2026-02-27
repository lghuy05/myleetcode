import requests

url = "https://api.open-meteo.com/v1/forecast"


params = {
    "latitude": 27.9506,
    "longitude": -82.4572,
    "current_weather": True
}

response = requests.get(url, params=params)

data = response.json()

print(data)
print("Temperature:", data["current_weather"]["temperature"])


