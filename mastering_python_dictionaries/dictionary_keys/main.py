authors_books = {
    'William Shakespeare': ['Hamlet', 'Macbeth', 'Romeo and Juliet', 'Othello'],
    'J.K. Rowling': ['Harry Potter and the Sorcerer\'s Stone', 'Harry Potter and the Chamber of Secrets', 'Harry Potter and the Prisoner of Azkaban', 'Harry Potter and the Goblet of Fire'],
    'George Orwell': ['1984', 'Animal Farm', 'Coming Up for Air'],
    'Stephen King': ['It', 'The Shining', 'Carrie', 'Misery'],
    'Agatha Christie': ['Murder on the Orient Express', 'The Murder of Roger Ackroyd', 'And Then There Were None', 'Death on the Nile']
}

# dict.keys() method gets the keys of a dictionary and returns 
# them as a list. A view object of type dict_keys is generated
# But is iterable (you can loop over it directly).
keys = authors_books.keys()
# Initialize the variable all_books as a list of all available book titles.
# Yes, it's empty
all_books = []

for author in keys:
    # iterates through each key in the dictionary
    # previously we created a list of keys or authors_books
    # Now we are iterating through this list of authors
    for book in authors_books[author]:
        #iterates through the value of each keys
        #iterates through the list of books for a given author
        print(f"{author}: {book}")
        # I am printing each book to show the iteration in action
        all_books.append(book)
        
# Testing
print("The list of all books in the library:", all_books)