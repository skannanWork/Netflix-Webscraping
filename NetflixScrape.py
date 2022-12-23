import json

# Load the Netflix data from a JSON file
with open("netflix_data.json", "r") as f:
    netflix_data = json.load(f)

# Extract the list of movies and TV shows from the data
movies = netflix_data["movies"]
tv_shows = netflix_data["tv_shows"]

# Calculate the total number of movies and TV shows
total_movies = len(movies)
total_tv_shows = len(tv_shows)

# Calculate the total runtime of all the movies and TV shows
total_movie_runtime = sum(movie["runtime"] for movie in movies)
total_tv_show_runtime = sum(
    episode["runtime"] for tv_show in tv_shows for season in tv_show["seasons"] for episode in season["episodes"]
)
total_runtime = total_movie_runtime + total_tv_show_runtime

# Calculate the average rating of all the movies and TV shows
total_movie_ratings = sum(movie["rating"] for movie in movies)
total_tv_show_ratings = sum(
    episode["rating"] for tv_show in tv_shows for season in tv_show["seasons"] for episode in season["episodes"]
)
total_ratings = total_movie_ratings + total_tv_show_ratings
average_rating = total_ratings / (total_movies + total_tv_shows)

# Print the results
print(f"Total number of movies: {total_movies}")
print(f"Total number of TV shows: {total_tv_shows}")
print(f"Total runtime: {total_runtime} minutes")
print(f"Average rating: {average_rating:.1f}")