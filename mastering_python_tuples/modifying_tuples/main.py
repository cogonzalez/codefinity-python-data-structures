movie_genres = ("Action", "Comedy", "Drama", "Horror", "Sci-Fi")

# Write your code here
# Convert the tuple into a list and assign it to the variable temp_list.
temp_list = list(movie_genres)

# Replace the element "Drama" with "Thriller".
# Replace the element "Horror" with "Adventure".

temp_list[temp_list.index("Drama")] = "Thriller"  
temp_list[temp_list.index("Horror")] = "Adventure"  

# Convert the list back into a tuple and assign the value to the variable movie_genres.
movie_genres = tuple(temp_list)

# Delete the temporary list.
del temp_list

# Testing
print("Updated genres:", movie_genres)