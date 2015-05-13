import json
import requests
from flask import Flask, render_template, jsonify, url_for


# Create a Flask application
app = Flask(__name__)


# Define some routes
@app.route('/')
def index():
    """Renders the home page with some data."""

    data = {}
    data['title'] = 'Saluton, Mondo!'
    data['body'] = """<p>This is a quick demo of how you can wire up a quick
        website with Flask and an API. You might normally get this text from your
        database, or you could insert it directly in a template. See the template
        for an example&mdash;this text is from app.py, but the button below is from
        the template.</p>"""

    # Render a template with the content of the data dictionary
    return render_template('index.html', data=data)


@app.route('/asteroids')
def asteroids():
    """Renders the asteroids page. The actual data will be fetched with
    JavaScript."""

    data = {}
    data['title'] = 'List of Asteroids'
    data['body'] = """<p>This page uses JavaScript to render a table of Asteroid
        data. Python gets the data from an external API. JavaScript in the
        browser then gets that JSON and displays it with a Handlebars template.
        Look at the source code for comments.</p>"""

    return render_template('asteroids.html', data=data)


@app.route('/api/asteroids')
def asteroids_api():
    """Fetches and displays 10 asteroids as JSON."""

    # Don't do it like this on a real application. You should be polite and
    # cache the data so that you don't hit the external API on every page load.
    query = 'http://www.asterank.com/api/asterank?query={%22e%22:{%22$lt%22:0.1},%22i%22:{%22$lt%22:4},%22a%22:{%22$lt%22:1.5}}&limit=10'

    # Fetch the JSON from the external API
    json_string = requests.get(query)

    data = {}
    data['asteroids'] = json.loads(json_string.text)

    # You could cache it and manipulate it before sending it to the browser,
    # but this example is just going to send it to the browser.
    return jsonify(data)

if __name__ == '__main__':
    app.debug = True
    app.run(port=5005)
