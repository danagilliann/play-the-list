from pprint import pprint

class Track:
    def __init__(self, name, playback_fav, genres):
        self.name = name
        self.playback_fav = playback_fav
        self.genres = genres
        self.next = None

    def set_next(track):
        self.next = track

class Track_List:
    def __init__(self, head):
        self.head = head

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

def get_linked_list(array):
    song_list = Track_List(array[0])
    node = song_list.head

    for i in range(0,len(array) - 1):
        node.next = array[i + 1]
        node = node.next

    return song_list

def print_linked_list(linked_li):
    node = linked_li.head

    while node != None:
        pprint(vars(node))
        print("\t", node.next)
        node = node.next

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

    track_nodes = get_linked_list(track_nodes)
    print_linked_list(track_nodes)

    # for node in track_nodes:
    #     pprint(vars(node))
    # pprint(vars(node))
    # pprint(track.get('playback_count'))
