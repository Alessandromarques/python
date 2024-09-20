import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
from dotenv import load_dotenv

# Substitua com suas próprias credenciais
load_dotenv()
client_id = os.getenv('SPOTIFY_CLIENT_ID')
client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')

# Configurando as credenciais do cliente
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

# Testando a conexão: Buscando informações sobre uma faixa
track = sp.track('spotify:track:3n3Ppam7vgaVa1iaRUc9Lp')
print(track)
