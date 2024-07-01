""" Helping Function """
import requests
from dotenv import load_dotenv

WEATHER_API_KEY = load_dotenv('WEATHER_API_KEY')

def get_location_and_temperature(client_ip: str) -> any:
    """ Get Location and Temperature data """
    response = requests.get(f'http://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q=${client_ip}')
    jsonResponse = response.json()

    return jsonResponse.location.city, round(jsonResponse.current.temp_c)
