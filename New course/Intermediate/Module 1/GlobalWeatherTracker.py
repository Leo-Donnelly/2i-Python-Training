import random

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
        fakeConditions = ["Cloudy", "Rainy", "Snowy", "Thunderstorming", "Clear"]
        self.weather_records[city] = Weather(
            temperature=random.randint(-5,35),
            condition=random.choice(fakeConditions),
            humidity=random.randint(30,90),
        )
        
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