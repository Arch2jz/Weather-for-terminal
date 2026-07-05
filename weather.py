import requests
import os
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")

city = input("Enter city name: ")

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"



response = requests.get(url)
data = response.json()


if data["cod"] != "404":
    temp = data["main"]["temp"]
    weather = data["weather"][0]["description"]

    print(f"\nWeather in {city}:")
    print(f"Temperature: {temp}°C")
    print(f"Condition: {weather}")
else:
    print("City not found 😭")