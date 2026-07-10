
animal_movies = ('The Lion King', 'Jurassic Park', 'Finding Nemo')

# Write your code here
temp_list = list(animal_movies)
temp_list.append('Dumbo')
temp_list.append('Zootopia')
# Convert to List Method
animal_movies = tuple(temp_list)

print("Updated animal movies:", animal_movies)




# ********** Alternative if he new list was 100 long *********************
# ********** And you had to resort the list          ********************
animal_movies = ('The Lion King', 'Jurassic Park', 'Finding Nemo')

# Write your code here
new_movies = ['Dumbo','Zootopia']

# Convert to List Method so you can modify using list.methods()
temp_list = list(animal_movies)
temp_list = temp_list + new_movies
temp_list.remove("The Lion King")
temp_list = sorted(temp_list)

# Convert to List Method
animal_movies = tuple(temp_list)

print("Updated animal movies:", animal_movies)


# ****************************************************************

animal_movies = ('The Lion King', 'Jurassic Park', 'Finding Nemo')

# Write your code here
new_movies = ("Dumbo", "Zootopia")

# Concantenate method
animal_movies += new_movies

print("Updated animal movies:", animal_movies)




