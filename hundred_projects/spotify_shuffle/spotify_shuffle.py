import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json


rc = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="a4df536e1dfd42268cb98c91779c6096",
                                               client_secret="1d2fc9802d754d8f8f52fcb4bec9b6ec",
                                               redirect_uri="http://localhost:7777/callback",
                                               scope="user-read-playback-state"))


mc = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="a4df536e1dfd42268cb98c91779c6096",
                                               client_secret="1d2fc9802d754d8f8f52fcb4bec9b6ec",
                                               redirect_uri="http://localhost:7777/callback",
                                               scope="user-modify-playback-state"))                                           



recs = rc.recommendations(seed_genres=["dubstep"], limit=10)

with open("deneme.json", 'w') as w:
    json.dump(recs, w)


for track in recs["tracks"]:
    print(track["name"])
    mc.add_to_queue(track["uri"])
    print("\n")


