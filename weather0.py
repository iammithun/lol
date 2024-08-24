# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 09:51:32 2024

@author: iamrs
"""

import requests

def get_weather(api_key, location):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    if data["cod"] == 200:
        return data["main"]["temp"], data["main"]["feels_like"]
    else:
        return None, None

def main():
    api_key = "YOUR_API_KEY"  # Replace "YOUR_API_KEY" with your actual API key
    location = input("Enter location: ")
    temp, feels_like = get_weather(api_key, location)
    if temp is not None:
        print(f"Temperature in {location}: {temp}°C")
        print(f"Feels like: {feels_like}°C")
    else:
        print("Failed to retrieve weather data.")

if __name__ == "__main__":
    main()
