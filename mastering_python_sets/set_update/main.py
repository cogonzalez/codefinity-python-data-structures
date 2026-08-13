# Example #1 
print("Example #1 ***************************")
# Original set of favorite movies
favorite_movies = {"Inception", "Interstellar", "Tenet"}
print(f"Number of movies in Favorites:", {len(favorite_movies)})
# Adding multiple new movies
favorite_movies.update(["Tenet", "Memento", "The Prestige"])
# Print the updated set adds the new movies to favorite_movies,
# disregards duplicates, so the new updated set has no duplicates
print(f"Number of movies in Favorites:", {len(favorite_movies)})
print(favorite_movies)

print("Main Output **************************")
marvel_movies = {
    'Avengers: Endgame',
    'Black Panther',
    'Iron Man'
}
movies_to_add = ('Spider-Man: No Way Home', 'Guardians of the Galaxy')

# Write your code here
marvel_movies.update(movies_to_add)
# Testing
print("Updated set:", marvel_movies)