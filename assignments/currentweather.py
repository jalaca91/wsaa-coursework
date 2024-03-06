# Author: Jaime Lara Carrillo

# Get two sources of data: temperature and wind speed
import requests
url = " https://api.open-meteo.com/v1/forecast?latitude=53.82&longitude=-9.5&current=temperature_2m"
response = requests.get(url)
data_temp = response.json()

url = " https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
response = requests.get(url)
data_wind = response.json()

# Print out the current temperature 
current_temperature = data_temp["current"]["temperature_2m"]
print("The current temperature is:", current_temperature, "°C")

# Print out the current wind speed 
current_wind_speed = data_wind["current"]["wind_speed_10m"]
print("The current wind speed is:", current_wind_speed, "m/s")