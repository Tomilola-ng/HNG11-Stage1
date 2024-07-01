""" Helping Function """
import requests
from dotenv import load_dotenv

WEATHER_API_KEY = load_dotenv('WEATHER_API_KEY')

def get_my_ip():
    """ Return IP """
    return requests.get('https://api.ipify.org').text

def get_location_and_temperature(client_ip: str) -> any:
    """ Get Location and Temperature data """
    print(WEATHER_API_KEY, client_ip)

    response = requests.get(f'http://api.weatherapi.com/v1/current.json?key=269eca5dce734a71972204904240107&q={client_ip}')
    json_response = response.json()

    return json_response['location']['region'], round(json_response['current']['temp_c'])
