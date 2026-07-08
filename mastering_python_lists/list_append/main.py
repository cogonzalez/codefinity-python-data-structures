travel_wishlist = ['Paris', 'Tokyo']

# Write your code below
travel_wishlist.append("Berlin")
travel_wishlist.append("New York")

# Testing
print("Updated list:", travel_wishlist)

# Alternatively ***********
travel_wishlist = ['Paris', 'Tokyo']
additional_cities = ["Berlin", "New York"]

# iterate through the additional_cities to append each one
# is the additional_cities list was extremely long
# iterating through the list would be much better.
for city in additional_cities:
    travel_wishlist.append(city)
# Testing
print("Iterated list:", travel_wishlist)
