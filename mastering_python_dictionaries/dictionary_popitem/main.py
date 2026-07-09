authors_books = {
    'William Shakespeare': ['Hamlet', 'Macbeth', 'Romeo and Juliet', 'Othello'],
    'J.K. Rowling': ['Harry Potter and the Sorcerer\'s Stone', 'Harry Potter and the Chamber of Secrets', 'Harry Potter and the Prisoner of Azkaban', 'Harry Potter and the Goblet of Fire'],
    'George Orwell': ['1984', 'Animal Farm', 'Coming Up for Air'],
    'Stephen King': ['It', 'The Shining', 'Carrie', 'Misery'],
    'Agatha Christie': ['Murder on the Orient Express', 'The Murder of Roger Ackroyd', 'And Then There Were None', 'Death on the Nile']
}

# Write your code here
removed_element = authors_books.popitem()

key_to_add = 'Mark Twain'
value_to_add = ['The Adventures of Tom Sawyer', 'Adventures of Huckleberry Finn', 'The Prince and the Pauper']

authors_books[key_to_add] = value_to_add

# Testing
print("Removed element:", removed_element)
print("Updated dictionary:", authors_books)