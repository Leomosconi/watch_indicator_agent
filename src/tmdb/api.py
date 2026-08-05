import os
import requests
from dotenv import load_dotenv

load_dotenv()

class ApiTMDB:
    def __init__(self):
        self.api_key = os.getenv("TMDB_API_KEY")
        self.base_url = "https://api.themoviedb.org/3"

    def authenticate(self):
        try:
            url = f"{self.base_url}/authentication"
            headers = {
                "accept": "application/json",
                "Authorization": f"Bearer {self.api_key} "
            }
            response = requests.get(url, headers=headers)

            print(response.status_code)
        except Exception as e:
            print("Error authenticating with TMDB API:", e)

    def get_movie(self):
        try:
            url = f"{self.base_url}/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&sort_by=popularity.desc"
            headers = {
                "accept": "application/json",
                "Authorization": f"Bearer {self.api_key}"
            }
            response = requests.get(url, headers=headers)
            print(response.text)
        except Exception as e:
            print("Error fetching movie data from TMDB API:", e)
