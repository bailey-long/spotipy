import spotipy
from spotipy.oauth2 import SpotifyOAuth
import random
import secrets as s

SPOTIPY_CLIENT_ID = s.SPOTIPY_CLIENT_ID
SPOTIPY_CLIENT_SECRET = s.SPOTIPY_CLIENT_SECRET
SPOTIPY_REDIRECT_URI = s.SPOTIPY_REDIRECT_URI

# Set up Spotipy with the credentials
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET,
    redirect_uri=SPOTIPY_REDIRECT_URI,
    scope='playlist-modify-public'
))

# Function to search for tracks based on the genre
def search_tracks_by_genre(genre, limit=50):
    results = sp.search(q=f'genre:{genre}', type='track', limit=limit)
    tracks = results['tracks']['items']
    return tracks

# Function to create a playlist
def create_playlist(name, description, tracks):
    user_id = sp.me()['id']
    playlist = sp.user_playlist_create(user_id, name, public=True, description=description)
    playlist_id = playlist['id']
    track_uris = [track['uri'] for track in tracks]
    sp.playlist_add_items(playlist_id, track_uris)

# Main function
def main():
    #ANCHOR Define your genre (you can change it to match your preferences)
    genre = 'noise%rock'

    # Search for noise core tracks
    tracks = search_tracks_by_genre(genre)

    if not tracks:
        print(f"No {genre} tracks found.")
        return

    # Shuffle the tracks to add variety
    random.shuffle(tracks)

    # Create a playlist with the noise core tracks
    playlist_name = 'Noise Core Playlist'
    playlist_description = 'A playlist of noise core songs generated with Spotipy.'
    create_playlist(playlist_name, playlist_description, tracks)

    print(f"Playlist '{playlist_name}' created successfully.")

if __name__ == "__main__":
    main()
