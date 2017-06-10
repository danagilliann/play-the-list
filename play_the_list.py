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
    # track = client.get('/resolve', url='http://soundcloud.com/forss/flickermood')
    # print(track.id)
    playlist = client.get('/resolve', url='http://soundcloud.com/sadier/sets/heaven_set')
    tracks = playlist.tracks
    pprint(len(tracks))
    # pprint(vars(playlist))
    # tracks = client.get('/tracks', limit=10)
    # for track in tracks:
    #     print(track.title)
    return render_template('main.html')

# @app.route('/omg', strict_slashes=False)
# def omg():
#     return 'OMG'
