from pprint import pprint

class Track:
    def __init__(self, name, playback_fav):
        self.name = name
        self.playback_fav = playback_fav

def song_sorter(tracks={}):
    track_nodes = []

    for track in tracks:
        playback_fav = 0
        playback = track.get('playback_count')
        favoritings = track.get('favoritings_count')

        if playback == None and favoritings == None:
            playback_fav = 0
        elif playback == None:
            playback_fav = favoritings
        elif favoritings == None:
            playback_fav = playback
        else:
            playback_fav = playback + favoritings

        track_nodes.append(Track(
            track.get('title'), playback_fav))

    for node in track_nodes:
        pprint(vars(node))
        # pprint(vars(node))
    # pprint(track.get('playback_count'))
