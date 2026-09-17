import os
import requests
from datetime import datetime
import json

def get_token():
	from dotenv import load_dotenv
	load_dotenv()
	token = os.getenv('TOKEN_TMDB')
	if not token:
		raise RuntimeError('TOKEN_TMDB nao foi encontrado no arquivo .env')
	return token

def get_movie(token):
	url = "https://api.themoviedb.org/3/discover/movie"

	headers = {
	"accept": "application/json",
	"Authorization": f'Bearer {token}'
	}

	params = {
	"page": 1,
	}

	response = requests.get(url, headers=headers)
	pages = response.json()["total_pages"]

	print(pages)

	# for i in pages:
	# 	response = requests.get(url, headers=headers, params=params)


	headers
	return json.dumps(response.json())

def save_to_bronze(data, file_format, schema, table):
	day = datetime.now()
	date = day.strftime("%Y-%m-%d")
	path = f"./data/bronze/{schema}/{table}/{date}/"
	os.makedirs(path, exist_ok=True)

	with open(os.path.join(path, f"{day.strftime('%Y-%m-%d %H-%M-%S-%f')}.{file_format}"), "w") as f:
		f.write(data)


token = get_token()
movie = get_movie(token)

# save_to_bronze(movie, "json", "themoviedb", "movie")