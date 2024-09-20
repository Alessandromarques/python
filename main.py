import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Substitua com suas próprias credenciais
client_id = 'a38ea325ada847b8b1e94b4b487cf871'
client_secret = 'd41c593b0baa4ef2a3b0e18c26982f5e'

# Configurando as credenciais do cliente
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

# Testando a conexão: Buscando informações sobre uma faixa
track = sp.track('spotify:track:3n3Ppam7vgaVa1iaRUc9Lp')
print(track)
