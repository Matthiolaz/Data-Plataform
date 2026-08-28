import os

import requests
from dotenv import load_dotenv

load_dotenv()

token = os.getenv('TOKEN_TMDB')
if not token:
	raise RuntimeError('TOKEN_TMDB nao foi encontrado no arquivo .env')

url = 'https://api.themoviedb.org/3/discover/movie'     
headers = {
	"accept": "application/json",
	'Authorization': f'Bearer {token}'
}

print(token)

response = requests.get(url, headers=headers)

print(response.content)