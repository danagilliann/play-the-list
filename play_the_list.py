# libraries
from flask import Flask
from flask import render_template
import soundcloud

# dev
from pprint import pprint
import config

client = soundcloud.Client(
        client_id=config.client_id(),
        client_secret=config.client_secret(),
        username=config.username(),
        password=config.password()
)
app = Flask(__name__)

@app.route('/')
def main():
    playlist = client.get('/resolve', url='https://soundcloud.com/dana-lee-34/sets/all-techno')
    tracks = playlist.tracks

    for track in tracks:
        pprint(track.get('playback_count'))

    return render_template('main.html')

# @app.route('/omg', strict_slashes=False)
# def omg():
#     return 'OMG'
