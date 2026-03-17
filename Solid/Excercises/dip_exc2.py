# Before: WeatherApp is tightly coupled to OpenWeatherMapAPI
class OpenWeatherMapAPI:
    def fetch_weather(self, city: str) -> str:
        print(f"Calling OpenWeatherMap API for: {city}")
        return "Sunny, 25C"

class WeatherApp:
    def __init__(self):
        self.api = OpenWeatherMapAPI()  # Direct dependency!

    def display_weather(self, city: str) -> None:
        weather = self.api.fetch_weather(city)
        print(f"Weather in {city}: {weather}")

if __name__ == "__main__":
    app = WeatherApp()
    app.display_weather("London")

# TODO: Create a WeatherProvider ABC with a get_weather(city) method.
# TODO: Refactor WeatherApp to accept a WeatherProvider via its constructor.

from abc import ABC, abstractmethod

class WeatherProvider(ABC):

    @abstractmethod
    def fetch_weather(self, city):
        pass

class OpenWeather(WeatherProvider):

    def fetch_weather(self, city: str) -> str:
        print(f"Calling OpenWeatherMap API for: {city}")
        return "Sunny, 25C"
    
class AccuWeather(WeatherProvider):

    def fetch_weather(self, city: str) -> str:
        print(f"Calling OpenWeatherMap API for: {city}")
        return "Sunny, 25C"
    

class NewWeatherApp:

    def __init__(self, api):
        self.api = api  # dependency inversion

    def display_weather(self, city: str) -> None:
        weather = self.api.fetch_weather(city)
        print(f"Weather in {city}: {weather}")



if __name__ == "__main__":
    app = WeatherApp()
    app.display_weather("London")
    provider = AccuWeather()
    newapp = NewWeatherApp(provider)
    newapp.display_weather('London')