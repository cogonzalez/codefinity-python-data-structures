# Write your code here
space_movies = ('2001: A Space Odyssey', 'Interstellar', 'Star Wars: Episode IV - A New Hope', 'Gravity', 'The Martian')

# Testing
print("Movies about space:", space_movies)

movie_list = ["Inception", "Interstellar", "Tenet"]
print(movie_list, " - this is a list")
movies_tuple = tuple(movie_list)
print(movies_tuple, " - this is a tuple")

movie_title = tuple("Inception")
print(movie_title," - tuple is created with tuple()")
print(type(movie_title))

empty_tuple = ()          # empty tuple
print(empty_tuple, " - this is an empty tuple")
print(type(empty_tuple))

not_a_tuple = ("Inception") # string not a tuple needs a comma
print(not_a_tuple, " -  this is a string not a tuple")
print(type(not_a_tuple))

single_movie = ("Inception",)  # Single-element tuple
print(single_movie, " - this is a single-element tuple b/c of the comma")
print(type(single_movie))