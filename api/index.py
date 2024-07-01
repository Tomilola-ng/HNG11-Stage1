""" VIEW CONTRLLER """

from flask import Flask, render_template, request, jsonify, redirect
import requests

app = Flask(__name__)

@app.route('/')
def home():
    """ Main Code """
    return render_template('intro.html')

@app.route('/api')
def api():
    """ Redirect """
    return redirect('/api/hello')

@app.route('/api/hello')
def hello():
    """ Route to handle task """
    visitor_name = request.args.get('visitor_name', 'Guest')
    client_ip = request.remote_addr

    location, temperature = get_location_and_temperature(client_ip)

    response = {
        "client_ip": client_ip,
        "location": location,
        "greeting": f"Hello, {visitor_name}! The temperature is {temperature} degrees Celsius in {location}"
    }

    return jsonify(response)

def get_location_and_temperature(ip: str) -> any:
    """Get Location and Temperature data"""
    location_response = requests.get(f'https://ipapi.co/{ip}/json/')
    location_data = location_response.json()
    city = location_data.get('city', 'Unknown')
    
    api_key = '67f622ac7877aabc1e1d01982064e788'
    weather_response = requests.get(
        f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric')
    weather_data = weather_response.json()
    temperature = weather_data['main']['temp']

    return city, round(temperature)

if __name__ == '__main__':
    app.run(debug=True)
