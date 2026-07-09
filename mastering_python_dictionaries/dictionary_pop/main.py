authors_books = {
    'William Shakespeare': ['Hamlet', 'Macbeth', 'Romeo and Juliet', 'Othello'],
    'J.K. Rowling': ['Harry Potter and the Sorcerer\'s Stone', 'Harry Potter and the Chamber of Secrets', 'Harry Potter and the Prisoner of Azkaban', 'Harry Potter and the Goblet of Fire'],
    'George Orwell': ['1984', 'Animal Farm', 'Coming Up for Air'],
    'Stephen King': ['It', 'The Shining', 'Carrie', 'Misery'],
    'Agatha Christie': ['Murder on the Orient Express', 'The Murder of Roger Ackroyd', 'And Then There Were None', 'Death on the Nile']
}

for author in authors_books:
    for book in authors_books[author]:
        print(f"{author}: {book}")

# Write your code here
kings_books = authors_books.pop("Stephen King")

# Testing 
print(f"Updated dictionary: {authors_books}.\nStephen King\'s books: {kings_books}")

for author in authors_books:
    for book in authors_books[author]:
        print(f"{author}: {book}")
