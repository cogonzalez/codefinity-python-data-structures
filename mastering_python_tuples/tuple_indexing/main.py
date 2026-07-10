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
fight_club_index = drama_movies.index('Fight Club')
# Testing
print("The 'Fight Club' movie is at index:", fight_club_index)

# ****************************
dreamworks = (
    'Shrek the Halls',
    'Monsters vs. Aliens',
    'Madagascar',
    'Scared Shrekless',
    'Kung Fu Panda',
    'Dragons',
    'Madagascar',
    'Trolls Holiday',
    'How to Train Your Dragon',
    'Trolls',
    'Madagascar'
    )

# One at a time *****************************
first = dreamworks.index('Madagascar')
second = dreamworks.index('Madagascar', first+1)
third = dreamworks.index('Madagascar', second+1)
#fourth = dreamworks.index('Madagascar', third+1)
print(first, second, third)

print('Alternative Search Method')
# Alternatively  ****************************
# You don't know how many times this itme is in the list
# You don't know when to stop searching
# If you search beyond the occurrance you get an error

s_item = 'Panda'
if dreamworks.count(s_item) > 0:
    stop = dreamworks.count(s_item)
    print(f"{s_item} found {stop} occurrence(s).")
else:
    print(f"{s_item} not found.")

found_index = 0 # this forces to start looking at index = 0
for i in range(0,stop):
    try:
        dreamworks.index(s_item,found_index+i)
        found_index = dreamworks.index(s_item,found_index+i)
        print(f"found at index: {found_index}")
    except:
        print('Item Not Found')






