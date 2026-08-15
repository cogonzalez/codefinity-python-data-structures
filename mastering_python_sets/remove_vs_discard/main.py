marvel_movies = {
    'Avengers: Endgame',
    'Black Panther',
    'Iron Man',
    'The Dark Knight',
    'Spider-Man: No Way Home',
    'Guardians of the Galaxy',
    'Justice League'
}

# Write your code here
# Remove specific movies using discard
marvel_movies.discard("The Dark Knight")
marvel_movies.discard("Justice League")

# Testing
print("Updated set:", marvel_movies)
print(f"The new list contains exactly:", len(marvel_movies), "movies")