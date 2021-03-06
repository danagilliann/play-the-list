class Track:
    def __init__(self, name, playback_fav, genres):
        self.name = name
        self.playback_fav = playback_fav
        self.genres = genres

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
                    track.get('genre')))

    track_nodes = sorted(
            track_nodes,
            key=lambda track: track.playback_fav,
            reverse=True)

    # pprint_array(track_nodes)
