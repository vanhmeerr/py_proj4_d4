class book :

    total_books = 0

    def __init__(self, title, author):
        # instances variables 
        self.title = title
        self.author = author
        # increment the total number of books
        book.total_books += 1

        # return the info and title of the book
    def get_info(self):
        return f"title: {self.title}, author: {self.author}"
    
    @classmethod 
    def get_total_books(cls):
        # return the total number of books
        return cls.total_books
    
    @staticmethod
    def is_valid_title(title):
        # check if the title is non empty 
        return isinstance(title, str) and len(title) > 0
    
    
book1 = book("To Kill a Mockingbird", "Harper Lee")
book2 = book("1984", "George Orwell")
    
    
if __name__ == "__main__":
    book1 = book("To Kill a Mockingbird", "Harper Lee")
    book2 = book("1984", "George Orwell")

    # Print information about each book
print(book1.get_info())  # Output: Title: To Kill a Mockingbird, Author: Harper Lee
print(book2.get_info())  # Output: Title: 1984, Author: George Orwell

    # Print the total number of books created
print(book.get_total_books())  # Output: 2

    # Check if a title is valid
print(book.is_valid_title("Some Title"))  # Output: True
print(book.is_valid_title(""))  # Output: False

