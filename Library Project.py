database = {}
admin_database = {
    "ClaytonADM": "ssrules!"
}

class Library:
    def __init__(self):
        self.library = []
        self.members = []

    def add_book(self, add_book):
        self.library.append(add_book)

    def show_books(self):
        print("Here are the current books in the library:\n"
              f"Make sure to use the ISBN number when checking out!\n")
        for books in self.library:
            if books.state == 0:
                print(f"{books.title}\n"
                      f"Author: {books.author}\n"
                      f"Date of Publication: {books.published_date}.\n"
                      f"ISBN: {books.isbn}\n"
                      f"\n")

    def show_members(self):
        print("Current Member List:")
        for member in self.members:
            print(f"{member.name}")

    def checkout_book(self):
        choice = int(input("Please enter the ISBN of the book: "))
        for books in self.library:
            if books.isbn == choice:
                books.state = 1
                print(f"You have checked out {books.title}")

lib = Library()

class Book:
    def __init__(self, title, author, isbn, published_date, state):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.published_date = published_date
        self.state = state

    @staticmethod
    def add_book():
        print("To add a book, please enter the following information:")
        title = input("Title: ")
        author = input("Author: ")
        date = input("Date of Publish: ")
        isbn = len(title) * len(author)
        state = 0
        new_book = Book(title, author, isbn, date, state)
        lib.add_book(new_book)
        welcome_menu()


class Member:
    def __init__(self, name, username, email, password, membership=0, books=0):
        self.name = name
        self.username = username
        self.email = email
        self.password = password
        self.membership = membership
        self.books = books
        self.members = []

    @staticmethod
    def new_member():
        print("Please enter the following information to register with this library.")
        mname = input("What is your name: ")
        musername = input("What do you want your username to be: ")
        memail = input("What is your email address: ")
        mpassword = input("What do you want your password to be: ")
        mmembership = 1
        mbooks = 0
        new_member = Member(mname, musername, memail, mpassword, mmembership, mbooks)
        lib.members.append(new_member)
        database.update({mname: {"User": musername, "Password": mpassword}})
        display_menu(mname)

def admin(admin_name):
    selection = 0
    print(f"Welcome Admin {admin_name}, please select from the following: ")
    print("1. Add Book to Library \n"
          "2. Revoke User Account Access \n"
          "3. Sign Out")
    choice = int(input("Please select an option (1, 2, 3): "))
    while selection == 0:
        if choice == 1:
            selection = 1
            Book.add_book()
        if choice == 2:
            pass
        if choice == 3:
            selection = 2
            welcome_menu()

def check_admin(admin_name, admin_password):
    for admin_check in admin_database.keys():
        if admin_check == admin_name:
            for password in admin_database.values():
                if password == admin_password:
                    admin(admin_name)

def check_signin():
    print("Please enter your username and password below:")
    user = input("Enter your username: ")
    password = input("Enter your password: ")
    check_admin(user, password)
    sign_in(user, password)

def welcome_menu():
    selection = 0
    print("Welcome to the MEAT Gang Library. Please sign in or register below")
    print("1. Sign In")
    print("2. Register")
    choice = int(input("Enter your selection (1 or 2): "))
    while selection == 0:
        if choice == 1:
            selection = 1
            check_signin()
        if choice == 2:
            selection = 1
            Member.new_member()

def sign_in(user_name, user_password):
    for keys in database.values():
        for values in keys.values():
            if values == user_name:
                for value in keys.values():
                    if value == user_password:
                        display_menu(user_name)
    print("ERROR: The username or password entered is incorrect.")

def display_menu(username):
    selection = 0
    while selection == 0:
        print(" ")
        print(f"Welcome to the MEAT Gang Library {username}, "
              f"\nplease choose what you would like to do below:")
        print("1. View Books in Library \n"
              "2. Check out a book \n"
              "3. View Members \n"
              "4. Sign Out \n")
        choice = int(input("Choose what you would like (1 or 2): "))
        if choice == 1:
            lib.show_books()
        if choice == 2:
            lib.checkout_book()
        if choice == 3:
            lib.show_members()
        if choice == 4:
            welcome_menu()

#Initalize the Library with multiple books
book1 = Book("To Kill A Mockingbird", "Harper E. Lee", 124342, 1960, 0)
book2 = Book("Touching Spirit Bear", "Harper E. Lee", 124343, 2001, 0)
book3 = Book("Harry Potter and the Sorcerers Stone", "J. K. Rowling", 124344, 1997, 0)
book4 = Book("Harry Potter and the Chamber of Secrets", "J. K. Rowling", 124345, 1998, 0)
book5 = Book("Harry Potter and the Prisoner of Azkaban", "J. K. Rowling", 124346, 1999, 0)
list_of_books_to_initialize = [book1, book2, book3, book4, book5]
for book in list_of_books_to_initialize:
    lib.add_book(book)

#Start the Welcome Menu!
welcome_menu()