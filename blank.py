url = "https://api.themoviedb.org/3/movie/{}?api_key=855215c1f3bcbc34e6e8900ff096b57e&language=en-US".format(
            movie_id)
        data = requests.get(url)
        data = data.json()
        poster_path = data['poster_path']
        full_path = "https://image.tmdb.org/t/p/w500/" + poster_path