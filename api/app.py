""" VIEW CONTRLLER """
from flask import Flask, render_template, request, jsonify, redirect
from . import helpers

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
    ip_addr = request.META.get('HTTP_X_FORWARDED_FOR').split(',')[0]

    location, temperature = helpers.get_location_and_temperature(ip_addr)

    response = {
        "client_ip": ip_addr,
        "location": location,
        "greeting": f"Hello, {visitor_name}! The temperature is{temperature} degrees Celsius in {location}"
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
