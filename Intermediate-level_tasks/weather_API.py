import requests
from datetime import datetime

# Your API endpoint
url = 'https://api.openweathermap.org/data/2.5/weather?q=Dhaka&appid=e7d703c87e5742aae02ef73c6ba49008'

# Sending the request to the API
response = requests.get(url)

# Parsing the JSON response
weather_data = response.json()

# Extracting and printing the information
if weather_data['cod'] == 200:
    temp_k = weather_data['main']['temp']
    temp_c = temp_k - 273.15  # Converting from Kelvin to Celsius
    weather_description = weather_data['weather'][0]['description']

    # Getting the date, month, and year
    date_time = datetime.fromtimestamp(weather_data['dt'])
    date_str = date_time.strftime("%Y-%m-%d %H:%M:%S")

    print(f"Date and Time: {date_str}")
    print(f"Temperature in Dhaka: {temp_c:.2f}°C")
    print(f"Weather description: {weather_description.capitalize()}")
else:
    print(f"Error: {weather_data['message']}")