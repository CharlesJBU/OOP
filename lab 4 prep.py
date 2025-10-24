class Customer:
    def __init__(self):
        self.cid = ""
        self.acc_no = ""
        self.cname = ""
        self.phone = ""
        self.emailid = ""
        self.balance = 0
        self.cc = []
        self.debit =""

    def create_customer(self):
        self.cc = []
        self.cid = input("enter new customer ID:")
        self.acc_no = int(input("enter account number:"))
        self.cname = input("enter customer name:")
        self.phone = int(input("enter phone number"))
        self.emailid = input("enter customer email:")
        self.balance = int(input("enter customer balance:"))
        c = int(input("how many cards would you like to enter:"))
        for i in range(0, c):
            self.cc.append(int(input("enter card number:")))
        self.debitcard = input("enter customer debit card:")

    def debit_from(self, amount):
        self.balance -= amount

    def credit_to(self, amount):
        self.balance += amount

    def display_all(self):
        print("Customer ID: ", self.cid)
        print("Account number: ", self.acc_no)
        print("Customer name: ", self.cname)
        print("Phone number: ", self.phone)
        print("Email address: ", self.emailid)
        print("Balance: ", self.balance)
        print("Credit cards: ", self.cc)
        print("Debit card: ", self.debitcard)

class Card:
    def __init__(self):
        self.ty = ""
        self.cn = ""
        self.cv = ""
        self.expdate = ""
        self.balance = 0
    def create_card(self):
        self.ty = input("enter card type:")
        self.cn = int(input("enter card number:"))
        self.cv = int(input("enter cvv number:"))
        self.expdate = input("enter expiration date:")
        self.balance = int(input("enter customer balance:"))
    def display_card(self):
        print("Card type: ", self.ty)
        print("Card number: ", self.cn)
        print("CVV number: ", self.cv)
        print("Expiration date: ", self.expdate)
        print("Balance: ", self.balance)

c1 = Customer()
c2 = Customer()

c1.create_customer()
c2.create_customer()

c1.debit_from(100)
c2.credit_to(100)

c1.display_all()
c2.display_all()

d1 = Card()
d2 = Card()

d1.create_card()
d2.create_card()

d1.display_card()
d2.display_card()
