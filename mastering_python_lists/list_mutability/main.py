# Initial travel wishlist with nested lists
travel_wishlist = [
    ["Paris", "France", 2000],
    ["Tokyo", "Japan", 3000],
    ["New York", "USA", 2500]
]

# Applying a 20% discount to the estimated cost
travel_wishlist[0][2] = travel_wishlist[0][2] * 0.8
travel_wishlist[1][2] = travel_wishlist[1][2] * 0.8
travel_wishlist[2][2] = travel_wishlist[2][2] * 0.8

# Printing the updated travel_wishlist to verify the change
print('Updated list:', travel_wishlist)

# Alternatively use a for loop to iterate through the list
# Initial travel wishlist with nested lists
# Restore List to Original
travel_wishlist = [
    ["Paris", "France", 2000],
    ["Tokyo", "Japan", 3000],
    ["New York", "USA", 2500]
]
print('Restored list:', travel_wishlist)
for i in range(0,len(travel_wishlist)):
    # [][] notation refers to outte list and inner list for nested lists
    # [i] will iterate through the list [-1] reffers to the last item in the inner list
    # why [-1] rather than [2], you always want the program to figure it out
    # you don't want to be counting yourself
    travel_wishlist[i][-1] = travel_wishlist[i][-1] * 0.8
print('Discounted list (using iteration):', travel_wishlist)
