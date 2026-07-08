travel_wishlist = ["Paris", "Oslo", "Kyoto", "Sydney"]

# Deleting element using list.remove() method
if 'Oslo' in travel_wishlist:
    travel_wishlist.remove('Oslo')
if 'Sydney' in travel_wishlist:
    travel_wishlist.remove('Sydney')

# NOTE: always check in item is in list otherwise you might get an error
# which will hault your program
# Note: you can use an if statement or a try except

# Testing
print('Updated list:', travel_wishlist)