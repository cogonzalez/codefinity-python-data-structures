movie_poster = ('The Lion King', 'Jurassic Park', 'Finding Nemo', '2001: A Space Odyssey', 'Interstellar', 'Gravity', 'The Martian')

# Write your code here
temp_list = list(movie_poster)

temp_list.remove("The Lion King")
temp_list.remove("Jurassic Park")

movie_poster = tuple(temp_list)

del temp_list

# Testing 
print("Updated movie poster:", movie_poster)