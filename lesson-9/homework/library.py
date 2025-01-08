class BookNotFoundException(Exception):
    pass

class BookAlreadyBorrowedException(Exception):
    pass

class MemberLimitExceededException(Exception):
    pass

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if len(self.borrowed_books) >= 3:
            raise MemberLimitExceededException("Member has reached the borrowing limit.")
        if book.is_borrowed:
            raise BookAlreadyBorrowedException("Book is already borrowed.")
        self.borrowed_books.append(book)
        book.is_borrowed = True

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.is_borrowed = False

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def borrow_book(self, member_name, book_title):
        member = self.find_member(member_name)
        book = self.find_book(book_title)
        if not book:
            raise BookNotFoundException("Book not found in the library.")
        member.borrow_book(book)

    def return_book(self, member_name, book_title):
        member = self.find_member(member_name)
        book = self.find_book(book_title)
        if book:
            member.return_book(book)

    def find_member(self, member_name):
        for member in self.members:
            if member.name == member_name:
                return member
        return None

    def find_book(self, book_title):
        for book in self.books:
            if book.title == book_title:
                return book
        return None

if __name__ == "__main__":
    library = Library()

    library.add_book(Book("The Lord of the Rings", "J.R.R. Tolkien"))
    library.add_book(Book("To Kill a Mockingbird", "Harper Lee"))
    library.add_book(Book("1984", "George Orwell"))

    library.add_member(Member("Alice"))
    library.add_member(Member("Bob"))

    try:
        library.borrow_book("Alice", "The Lord of the Rings")
        library.borrow_book("Alice", "To Kill a Mockingbird")
        library.borrow_book("Alice", "1984") 
    except MemberLimitExceededException as e:
        print(f"Error: {e}")

    try:
        library.borrow_book("Bob", "The Lord of the Rings") 
    except BookAlreadyBorrowedException as e:
        print(f"Error: {e}")

    try:
        library.borrow_book("Bob", "The Hobbit") 
    except BookNotFoundException as e:
        print(f"Error: {e}")

    library.return_book("Alice", "The Lord of the Rings")
    library.borrow_book("Bob", "The Lord of the Rings")