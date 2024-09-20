import requests

API_KEY = "74560d15aa07dc57c3dbab1187697d73"
MY_LAT = 29.963659
MY_LONG = 77.546028
owm_endpoint = "https://api.openweathermap.org/data/2.5/forecast?"

params = {
    "lat" : MY_LAT,
    "lon" : MY_LONG,
    "appid" : API_KEY,
    "units" : "metric",
}

# print(f"https://api.openweathermap.org/data/2.5/forecast?lat={MY_LAT}&lon={MY_LONG}&appid={API_KEY}&units=metric")
response = requests.get(owm_endpoint, params)
response.raise_for_status()
response_json = response.json()

print(response_json)
