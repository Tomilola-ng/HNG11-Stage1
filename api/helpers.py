""" Helping Function """
import os
import socket
import requests

from dotenv import load_dotenv
load_dotenv()

WEATHER_API_KEY = os.environ.get("WEATHER_API_KEY")

def get_my_ip():
    """ Return IP """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    s.connect(('8.8.8.8', 1))  # Using Google DNS server
    local_ip = s.getsockname()[0]
    s.close()
    return local_ip

def get_location_and_temperature(client_ip: str) -> any:
    """ Get Location and Temperature data """
    response = requests.get(f'http://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={client_ip}')
    json_response = response.json()

    return json_response['location']['region'], round(json_response['current']['temp_c'])
