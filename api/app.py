""" VIEW CONTRLLER """

from flask import Flask, render_template, request, jsonify, redirect

from helpers import get_location_and_temperature

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
    client_ip = request.remote_addr

    location, temperature = get_location_and_temperature(client_ip)

    response = {
        "client_ip": client_ip,
        "location": location,
        "greeting": f"Hello, {visitor_name}! The temperature is{temperature} degrees Celsius in {location}"
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
