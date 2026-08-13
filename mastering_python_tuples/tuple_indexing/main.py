drama_movies = (
    'The Shawshank Redemption',
    'Forrest Gump',
    'The Godfather',
    'A Beautiful Mind',
    'Fight Club',
    'The Green Mile',
    'The Pursuit of Happyness',
    'Schindler\'s List'
)

# Write your code here
# Testing
try:
    fight_club_index = drama_movies.index("Fight Club")
except ValueError:
    print("The 'Fight Club' movie is not found")
else:
    print("The 'Fight Club' movie is at index:", fight_club_index)

# Write your Alternative Code here
# Testing
try:
    fight_club_index = drama_movies.index("Fight ClubX")
except ValueError:
    print("The 'Fight ClubX' movie is not found")
else:
    print("The 'Fight ClubX' movie is at index:", fight_club_index)