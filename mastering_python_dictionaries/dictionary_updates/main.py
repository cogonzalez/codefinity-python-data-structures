authors_books = {
    'William Shakespeare': ['Hamlet', 'Macbeth', 'Romeo and Juliet', 'Othello'],
    'J.K. Rowling': ['Harry Potter and the Sorcerer\'s Stone', 'Harry Potter and the Chamber of Secrets', 'Harry Potter and the Prisoner of Azkaban', 'Harry Potter and the Goblet of Fire'],
    'George Orwell': ['1984', 'Animal Farm', 'Coming Up for Air'],
    'Stephen King': ['It', 'The Shining', 'Carrie', 'Misery'],
    'Agatha Christie': ['Murder on the Orient Express', 'The Murder of Roger Ackroyd', 'And Then There Were None', 'Death on the Nile']
}

print("Dictionary:", authors_books)
author_to_add = 'F. Scott Fitzgerald'
fitzgeralds_books = ['The Great Gatsby', 'Tender Is the Night', 'This Side of Paradise', 'The Beautiful and Damned', 'The Last Tycoon']

# Write your code here
authors_books[author_to_add]=fitzgeralds_books

# Testing
print("Updated dictionary:", authors_books)