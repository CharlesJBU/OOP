class User:
    def __init__(self, uid, name, password, address, phone, email):
        self.uid = ""
        self.name = ""
        self.password = ""
        self.address = ""
        self.phone = ""
        self.books = []
class Book:
    def __init__(self, bid, title, author, publisher, year):
        self.bid = ""
        self.title = ""
        self.author = ""
        self.publisher = ""
        self.year = ""

class Author:
    def __init__(self, aid, name, affiliation, country, phone, email):
        self.aid = ""
        self.name = ""
        self.affiliation = ""
        self.country = ""
        self.phone = ""
        self.email = ""

myUsers = {u1{name:"jerry george", password:"1234", adress:"3245 terracota drive", phone:"479-495-4958", email:"jerg@gmail.com"}}
myBooks = {}
myAuthors = {}

u1 = User(1, "jerry george", "1234", "3245 terracota drive", "479-495-4958", "jerg@gmail.com")
u2 = User(2, "henry hansen", "4321", "4896 oak place", "918-492-0289", "henryh@gmail.com")
u3 = User(3, "andrew anderson", "9374", "2431 birch plaza", "479-425-4857", "andrewa@gmail.com")

b1 = Book(1, "The Hobbit", "J.R.R. Tolkein", "penguin classics", "1965")
b2 = Book(2, "The Lord of the Rings", "J.R.R. Tolkein", "penguin classics", "1973")
b3 = Book(3, "Chronicles of Narnia", "C.S. Lewis","penguin classics", "1974")
b4 = Book(4, "Out of the Silent planet", "C.S. Lewis","penguin classics", "1956")
b5 = Book(5, "The Iliad", "Homer", "penguin classics", "1967")

def add_user(uid, name, password, address, phone, email):
    self.uid = input("enter user ID:")
    self.name = input("enter user name:")
    self.password = input("enter user password:")
    self.address = input("enter user address:")
    self.phone = input("enter user phone:")
    self.email = input("enter user email:")
    myUsers.update({uid: {"name": self.name,
                          "password": self.password,
                          "address": self.address,
                          "phone": self.phone,
                          "email": self.email,}})
    print(myUsers)


def add_books(self, bid, title, author, publisher, year):
    self.bid = input("enter book ID:")
    self.title = input("enter title:")
    self.author = input("enter author name:")
    self.publisher = input("enter publisher:")
    self.year = input("enter year:")

while True:
    print("press 1 to attribute books to user:")
    print("press 2 to display list:")
    print("press 3 to quit:")
    option = input("Select option:")
    if option == "1":
        add_user(uid, name, password, address, phone, email)

    if option == "2":
        add_books(self, bid, title, author, publisher, year)

    if option == "3":
        search = input("enter ID:")
        print(search)

