class User:
    def __init__(self, uid, name, password, address, phone, email):
        self.uid = uid
        self.name = name
        self.password = password
        self.address = address
        self.phone = phone
        self.books = []
class Book:
    def __init__(self, bid, title, author, publisher, year):
        self.bid = bid
        self.title = title
        self.author = author
        self.publisher = publisher
        self.year = year

class Author:
    def __init__(self, aid, name, affiliation, country, phone, email):
        self.aid = aid
        self.name = name
        self.affiliation = affiliation
        self.country = country
        self.phone = phone
        self.email = email

myBooks = []
myAuthors = []
myUsers = []

def add_user():
    newUser = {}
    uid = input("enter user ID:")
    name = input("enter user name:")
    password = input("enter user password:")
    address = input("enter user address:")
    phone = input("enter user phone:")
    email = input("enter user email:")
    newUser = {"uid":uid,
               "name":name,
               "password":password,
               "address":address,
               "phone":phone,
               "email":email,
               "books":[]}
    print(newUser)
    return newUser

def attribute_book():
    loaner_ID = input("enter loaner ID:")
    for user in myUsers:
        if user["uid"] == loaner_ID:
            user["books"].append(add_books())

def add_books():
    bid = input("enter book ID:")
    title = input("enter title:")
    author = input("enter author name:")
    publisher = input("enter publisher:")
    year = input("enter year:")
    newBook = {"bid":bid,
               "title":title,
               "author":author,
               "publisher":publisher,
               "year":year}
    return newBook

def add_author():
    aid = input("enter author ID:")
    name = input("enter author name:")
    affiliation = input("enter author affiliation:")
    country = input("enter author country:")
    phone = input("enter author phone:")
    email = input("enter author email:")
    newAuthor = {"aid":aid,
                 "name":name,
                 "affiliation":affiliation,
                 "country":country,
                 "phone":phone,
                 "email":email}
    return newAuthor

while True:
    print("press 1 to add user:")
    print("press 2 to print:")
    print("press 3 to attribute books to users:")
    print("press 4 to add authors:")
    print("press 5 to exit:")
    option = input("Select option:")
    if option == "1":
        myUsers.append(add_user())

    if option == "2":
        print(myUsers)
        print(myAuthors)
    if option == "3":
        attribute_book()

    if option == "4":
        add_author()

    if option == "5":
        exit(0)
