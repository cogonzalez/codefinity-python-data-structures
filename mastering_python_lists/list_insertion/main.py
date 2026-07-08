travel_wishlist = ["Paris", "Oslo", "Kyoto", "Sydney"]

# Adding new elements
# 0 is always the first position / index
travel_wishlist.insert(0,"London")
# So, after we have added and item 'Paris' is no longer in it's
# original position, so rather that manually counting
# we use: travel_wishlist.index('Paris')+1
# this gives us the new index and we + 1
travel_wishlist.insert(travel_wishlist.index('Paris')+1,"Budapest")

# Testing 
print("Updated travel_wishlist:", travel_wishlist)