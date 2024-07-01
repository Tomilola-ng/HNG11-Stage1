""" VIEW CONTRLLER """

import socket
from flask import Flask, render_template, request, jsonify, redirect

from . import helpers
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

app = Flask(__name__)

@app.route('/')
def home():
    """ Main Code """
    return render_template('/intro.html')

@app.route('/api')
def api():
    """ Redirect """
    return redirect('/api/hello')

@app.route('/api/hello')
def hello():
    """ Route to handle task """
    visitor_name = request.args.get('visitor_name', 'Guest')

    location, temperature = helpers.get_location_and_temperature(IPAddr)

    response = {
        "client_ip": IPAddr,
        "location": location,
        "greeting": f"Hello, {visitor_name}! The temperature is{temperature} degrees Celsius in {location}"
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
