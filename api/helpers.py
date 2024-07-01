""" Helping Function """
import environ
import get from requests

env = environ.Env()
environ.Env.read_env()

weather_api_key = env('WEATER_API_KEY')

def get_location_and_temperature(client_ip: str) -> any:
    """ Get Location and Temperature data """
    response = get(f'http://api.weatherapi.com/v1/current.json?key={weather_api_key}&q=${client_ip}')
    data = response.data

    print(data)

    return "lagos", "09.90"
