import spotipy
sp = spotipy.Spotify()

def play_artist(artist):
    results = sp.search(q=artist, limit=20)
    for i, t in enumerate(results['tracks']['items']):
        print ' ', i, t['name']
