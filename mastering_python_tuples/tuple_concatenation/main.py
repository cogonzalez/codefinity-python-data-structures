space_movies = ('2001: A Space Odyssey', 'Interstellar', 'Star Wars: Episode IV - A New Hope', 'Gravity', 'The Martian')

new_movies = ['The Lion King', 'Jurassic Park', 'Finding Nemo']

# Write your code here
animal_movies = tuple(new_movies)
print(animal_movies)

movie_poster = space_movies + animal_movies

# Testing
print("Now playing in theaters:", movie_poster)

# ************************************************************************
movie_titles = ("Inception", "Interstellar", "Dunkirk")
release_years = (2010, 2014, 2017)

# Concatenate the tuples to create a new tuple
combined_tuple = movie_titles + release_years

print(combined_tuple)