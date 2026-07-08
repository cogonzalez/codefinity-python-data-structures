travel_wishlist = ["Paris", "Oslo", "Kyoto", "Sydney", "Rome"]
print("Original list:", travel_wishlist)
# Write your code below
# 'Paris' is at the 0 position and Kyoto is at 2 position
del travel_wishlist[0]
# Now that the list has been modified Kyoto is at 1 position
print("Updated list:", travel_wishlist)
del travel_wishlist[1]
# Testing 
print("Updated list:", travel_wishlist)

# Problems is the every time you del the idexing changes
# Alternatively
travel_wishlist = ["Paris", "Oslo", "Kyoto", "Sydney", "Rome"]
print("ALt Original list:", travel_wishlist)
del travel_wishlist[travel_wishlist.index('Paris')]
print("Alt Updated list:", travel_wishlist)
del travel_wishlist[travel_wishlist.index('Kyoto')]
print("Alt Updated list:", travel_wishlist)

# More efficiently use remove no index required

travel_wishlist = ["Paris", "Oslo", "Kyoto", "Sydney", "Rome"]
print("ALt2 Original list:", travel_wishlist)
travel_wishlist.remove('Paris')    # deletes only the first occurance of 'Paris'
travel_wishlist.remove('Kyoto')    # deletes only the first occurance of 'Kyoto'
print("Alt2 Updated list:", travel_wishlist)




