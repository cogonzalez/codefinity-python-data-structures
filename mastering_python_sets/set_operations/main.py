# Ex#1 Define a set of favorite movies
moviesX = {"Inception", "Interstellar", "Tenet", "Dunkirk", "Memento"}
# Check if specific movies are in the set
is_inception_present = "Inception" in moviesX  # True
is_avatar_present = "Avatar" in moviesX        # False
# Print results
print(is_inception_present)  # Output: True
print("Inception" in moviesX) # prints output directly without creating a variable
print(is_avatar_present)     # Output: False
print("Avatar" in moviesX)    # prints output directly without creating a variable
print("Example # 1 **********************")

# Ex#2 Define a set of favorite movies
moviesY = {"Inception", "Interstellar", "Tenet", "Dunkirk", "Memento"}
# Iterate through the set and print each movie title
print("Movie collection:")
for movie in moviesY:
    print(movie)
print(f"Example # 2 ********************** \n ")


movies = {'The Shawshank Redemption', 'The Godfather', 'The Dark Knight', 'Pulp Fiction', 'Forrest Gump', 'Inception', 'Fight Club', 'The Matrix', 'The Lord of the Rings: The Return of the King', 'Star Wars: Episode IV - A New Hope', 'The Empire Strikes Back', 'The Godfather: Part II', 'Goodfellas', 'The Dark Knight Rises', 'The Silence of the Lambs', 'Schindler\'s List', 'City of God', 'The Usual Suspects', 'Seven Samurai', 'The Lion King', 'The Departed', 'Interstellar', 'Gladiator', 'Terminator 2: Judgment Day', 'Back to the Future', 'Casablanca', 'The Prestige', 'The Green Mile', 'The Shining', 'The Intouchables', 'The Pianist', 'Léon: The Professional', 'The Lord of the Rings: The Fellowship of the Ring', 'Pulp Fiction', 'Whiplash', 'The Wolf of Wall Street', 'The Revenant', 'The Social Network', 'The Terminator', 'The Big Lebowski', 'Saving Private Ryan', 'A Clockwork Orange', 'The Grand Budapest Hotel', 'The Incredibles', '12 Angry Men', 'The Hunt', 'The Conjuring'}

# Write your code here
is_first_movie_present = "The Green Mile" in movies

is_second_movie_present = "Titanic" in movies

is_third_movie_present = "Interstellar" in movies

# Testing
print(f"Presence of movies in the set:\nThe Green Mile: {is_first_movie_present};\nTitanic: {is_second_movie_present};\nInterstellar: {is_third_movie_present}.")