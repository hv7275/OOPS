class Book:
    def __init__(self, author, title):
        self.title = title
        self.author = author
        self.is_available = True
        
    def __str__(self):
        return f"{self.title} by {self.author}"
    

## Member Class

class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []
    
    
    def borrowed_book(self, book):
        if book.is_available:
            book.is_available = False
            
            self.borrowed_books.append(book)
            
            return f"{self.name} borrowed {book.title}"
        else:
            return f"{book.title} is not available"
        
    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_available = True
            self.borrowed_books.remove(book)
            return f"{self.name} returned {book.title}"
        else:
            return f"{self.name} does not have this book"
        
# Library Class
class Library:
    def __init__(self):
        self.books = []
        
    def add_book(self, book):
        self.books.append(book)
        return f"{book.title} added to library"
    
    def show_available_books(self):
        available = [book for book in self.books if book.is_available]
        if not available:
            return 'No books available'
        return '\n'.join(str(book) for book in available)


# Create library
library = Library()

# Create books
book1 = Book("Rowling", "Harry Potter")
book2 = Book("Orwell", "1984")

# Add books to library
print(library.add_book(book1))
print(library.add_book(book2))

# Create member
member1 = Member("Ali")

# Show available books
print("\nAvailable Books:")
print(library.show_available_books())

# Borrow book
print(member1.borrowed_book(book1))

# Show available books again
print("\nAvailable Books:")
print(library.show_available_books())

# Return book
print(member1.return_book(book1))

# Show again
print("\nAvailable Books:")
print(library.show_available_books())
