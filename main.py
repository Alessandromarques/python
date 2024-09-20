import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
from dotenv import load_dotenv

def listar_episodios_podcast(client_id, client_secret, show_id):
    """
    Função para listar todos os episódios de um podcast no Spotify.
    """
    auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(auth_manager=auth_manager)

    limit = 50
    offset = 0
    all_episodes = []

    while True:
        episodes = sp.show_episodes(show_id, limit=limit, offset=offset)
        all_episodes.extend(episodes['items'])

        if len(episodes['items']) < limit:
            break

        offset += limit

    return all_episodes

if __name__ == "__main__":
    # Substitua com suas próprias credenciais
    load_dotenv()
    client_id = os.getenv('SPOTIFY_CLIENT_ID')
    client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')
    # ID do podcast no Spotify (você encontra na URL do show)
    show_id = '768GVwxeh1o6kD5bD0qJeJ'

    episodios = listar_episodios_podcast(client_id, client_secret, show_id)

    # Exibir os episódios
    for episode in episodios:
        print(f"Título: {episode['name']}")
        print(f"ID do Episódio: {episode['id']}")
        print(f"Descrição: {episode['description'][:100]}...")
        print("="*50)

    print(f"Total de episódios encontrados: {len(episodios)}")