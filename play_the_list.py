# libraries
from flask import Flask, render_template, request
import soundcloud
from wtforms import Form, validators, StringField

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

class RegistrationForm(Form):
    playlist = StringField('Playlist', validators=[validators.input_required()])

class Track:
    def __init__(self, name, playback_fav, genres, url):
        self.name = name
        self.playback_fav = playback_fav
        self.genres = genres
        self.url = url

def pprint_array(array):
    for item in array:
        pprint(vars(item))

def get_playback_fav(playback, favoritings):
    playback_fav = 0

    if playback == None and favoritings == None:
        playback_fav = 0
    elif playback == None:
        playback_fav = favoritings
    elif favoritings == None:
        playback_fav = playback
    else:
        playback_fav = playback + favoritings

    return playback_fav

def get_song_nodes(tracks={}):
    track_nodes = []

    for track in tracks:
        playback_fav = get_playback_fav(
                track.get('playback_count'),
                track.get('favoritings_count'))
        track_nodes.append(
                Track(
                    track.get('title'),
                    playback_fav,
                    track.get('genre'),
                    track.get('permalink_url')))

    track_nodes = sorted(
            track_nodes,
            key=lambda track: track.playback_fav,
            reverse=True)

    return track_nodes
    # pprint_array(track_nodes)

@app.route('/', methods=['GET'])
def main():
    form = RegistrationForm(request.form)
    playlist = client.get('/resolve', url='https://soundcloud.com/dana-lee-34/sets/all-techno')
    tracks = playlist.tracks

    song_sorter.get_song_nodes(tracks)

    return render_template('main.html', form=True)

@app.route('/', methods=['POST'])
def main_post():
    playlist_link = request.form['playlist_link']
    print(playlist_link)

    playlist = client.get('/resolve', url=playlist_link)
    tracks = playlist.tracks

    track_nodes = get_song_nodes(tracks)
    pprint_array(track_nodes)

    return render_template('main.html', track_nodes=track_nodes)
# @app.route('/omg', strict_slashes=False)
# def omg():
#     return 'OMG'
