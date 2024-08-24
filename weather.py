# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 09:54:44 2024

@author: iamrs
"""

import requests

def get_weather(api_key, location):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

def main():
    api_key = "YOUR_API_KEY"  # Replace "YOUR_API_KEY" with your actual OpenWeatherMap API key
    location = input("Enter location: ")
    weather_data = get_weather(api_key, location)
    
    print("API Response:", weather_data)  # Print API response for debugging
    
    if weather_data.get("cod") == 200:
        temperature = weather_data["main"]["temp"]
        feels_like = weather_data["main"]["feels_like"]
        print(f"Weather in {location}:")
        print(f"Temperature: {temperature}°C")
        print(f"Feels like: {feels_like}°C")
    else:
        print("Failed to retrieve weather data.")

if __name__ == "__main__":
    main()
