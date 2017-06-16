# libraries
from flask import Flask, render_template, request
import soundcloud
import song_sorter
from wtforms import Form, validators, StringField

# dev
from pprint import pprint
import config

class RegistrationForm(Form):
    playlist = StringField('Playlist', validators=[validators.input_required()])

client = soundcloud.Client(
        client_id=config.client_id(),
        client_secret=config.client_secret(),
        username=config.username(),
        password=config.password()
)
app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    form = RegistrationForm(request.form)
    playlist = client.get('/resolve', url='https://soundcloud.com/dana-lee-34/sets/all-techno')
    tracks = playlist.tracks

    song_sorter.get_song_nodes(tracks)

    return render_template('main.html', form=form)

# @app.route('/omg', strict_slashes=False)
# def omg():
#     return 'OMG'
