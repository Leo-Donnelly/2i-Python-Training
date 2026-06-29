import random
import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")

if API_KEY is None:
    raise ValueError("No API key found.")

class City:
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def __str__(self):
        return f"{self.name}, {self.country}"
    

class Weather:
    def __init__(self, temperature, condition, humidity):
        self.temperature = temperature
        self.condition = condition
        self.humidity = humidity

    def __str__(self):
        return f"{self.temperature} degrees, {self.condition}, {self.humidity}% of humidity"
    
class Tracker:
    def __init__(self):
        self.weather_records = {}

    def __len__(self):
        return len(self.weather_records)
    
    def add_cities(self, *cities):
        for city in cities:
            self.update_weather(city)

    def update_weather(self, city):
        url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city.name}"
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                data = response.json()
                weather = Weather(
                    temperature=data["current"]["temp_c"],
                    condition=data["current"]["condition"]["text"],
                    humidity=data["current"]["humidity"]
                )
            else:
                print(f"Error collecting weather info for {city}: {response.status_code}")
                weather = Weather(temperature=0, condition="Unknown", humidity=0)

        except Exception as e:
            print(f"Request failed for {city}: {e}")
            weather = Weather(temperature=0, condition="Unknown", humidity=0)

        self.weather_records[city] = weather
        
    def list_cities(self):
        for city, weather in self.weather_records.items():
            print(f"{city} -> {weather}\n")

if __name__ == "__main__":
    london = City("London", "UK")
    newYork = City("New York", "USA")
    Tokyo = City("Tokyo", "Japan")

    tracker = Tracker()
    tracker.add_cities(london, newYork, Tokyo)

    print(f"Total cities tracker: {len(tracker)}\n")
    tracker.list_cities()