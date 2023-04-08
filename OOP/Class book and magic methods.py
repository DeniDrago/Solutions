class Book:

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}"

    def __len__(self):
        return self.pages

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    def __lt__(self, other):
        return self.pages < other.pages


books = [
    Book("1984", "George Orwell", 328),
    Book("To Kill a Mockingbird", "Harper Lee", 281),
    Book("The Great Gatsby", "F. Scott Fitzgerald", 180),
    Book("Pride and Prejudice", "Jane Austen", 432),
    Book("The Catcher in the Rye", "J.D. Salinger", 234),
]


for book in books:
    print(book)

for book in books:
    print(len(book))

print(books[0] == books[0])
print(books[0] == books[1])

sorted_books = sorted(books)
for book in sorted_books:
    print(book)

print(Book("Animal Farm", "George Orwell", 141) in books)
print(Book("1984", "George Orwell", 328) in books)

print(max(books))
print(min(books))
