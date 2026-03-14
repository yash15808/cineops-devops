from django.shortcuts import render
import requests
import time

API_KEY = "c97532fa7afc9d029525522ad740a271"

def fetch_movies(url, params):

    for i in range(3):   # retry 3 times
        try:
            response = requests.get(url, params=params, timeout=5)

            if response.status_code == 200:
                return response.json().get("results", [])

        except requests.exceptions.RequestException as e:
            print("Retrying API request...", e)
            time.sleep(1)

    return []


def home(request):

    query = request.GET.get("q")

    if query:
        url = "https://api.themoviedb.org/3/search/movie"
        params = {
            "api_key": API_KEY,
            "query": query
        }
    else:
        url = "https://api.themoviedb.org/3/movie/popular"
        params = {
            "api_key": API_KEY
        }

    movies = fetch_movies(url, params)

    return render(request, "index.html", {"movies": movies})