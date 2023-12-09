import sys
import requests

def get_weather(city, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    
    # Construct the API request URL
    url = f"{base_url}?q={city}&appid={api_key}"
    
    try:
        # Make a GET request to the OpenWeatherMap API
        response = requests.get(url)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            weather_data = response.json()
            
            # Extract relevant information
            temperature = weather_data['main']['temp']
            description = weather_data['weather'][0]['description']
            
            # Print the weather information
            print(f"Weather in {city}:")
            print(f"Temperature: {temperature} Kelvin")
            print(f"Description: {description}")
            
        else:
            print(f"Error: Unable to fetch weather information. Status code: {response.status_code}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 3:
        print("Usage: python weather_script.py <city_name> <api_key>")
    else:
        # Get command-line arguments
        city_name = sys.argv[1]
        api_key = sys.argv[2]

        # Call the get_weather method with provided arguments
        get_weather(city_name,api_key)
