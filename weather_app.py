import requests

def get_weather_data(location, api_key):
    """
    Fetch weather data from OpenWeatherMap API for a given location.
    """
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": location,
        "appid": api_key,
        "units": "metric"  # Use "imperial" for Fahrenheit
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        data = response.json()
        return data
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as err:
        print(f"Error fetching data from the API: {err}")
    return None

def display_weather(data):
    """
    Display weather information extracted from the API response.
    """
    if data:
        city = data['name']
        country = data['sys']['country']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        weather_description = data['weather'][0]['description']

        print(f"\nWeather in {city}, {country}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Conditions: {weather_description.capitalize()}")
    else:
        print("No data to display.")

def main():
    print("Welcome to the Command-Line Weather App!")
    
    # Prompt the user for input
    location = input("Enter the city name or ZIP code: ").strip()
    
    api_key = 'ca97ddd6e3b60c24182b6a0493b64c58' 
    
    # Validate user input and fetch weather data
    if location:
        weather_data = get_weather_data(location, api_key)
        display_weather(weather_data)
    else:
        print("Invalid input. Please enter a valid city name or ZIP code.")

if __name__ == "__main__":
    main()
