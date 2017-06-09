from flask import Flask
from flask import render_template
import config
import soundcloud

client_id = config.client_id()
client_secret = config.client_secret()
client = soundcloud.Client(client_id=client_id)

app = Flask(__name__)

@app.route('/')
def main():
    # track = client.get('/resolve', url='http://soundcloud.com/forss/flickermood')
    # print(track.id)
    tracks = client.get('/tracks', limit=10)
    for track in tracks:
        print(track.title)
    return render_template('main.html')

# @app.route('/omg', strict_slashes=False)
# def omg():
#     return 'OMG'
