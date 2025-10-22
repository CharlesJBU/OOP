class Customer:
    def __init__(self):
        self.cid = ""
        self.acc_no = ""
        self.cname = ""
        self.phone = ""
        self.emailid = ""
        self.balance = 0
    def create_customer(self):
        self.cid = input("enter new customer ID:")
        self.acc_no = int(input("enter account number:"))
        self.cname = input("enter customer name:")
        self.phone = int(input("enter phone number"))
        self.emailid = input("enter customer email:")
        self.balance = int(input("enter customer balance"))

    def debit_from(self, amount):
         self.balance -= amount

    def credit_to(self, amount):
         self.balance += amount

    def display_all(self):
        print("Customer ID: ", self.cid)
        
#main code
#  i = 1
# while true:
#     print("To create customer account press 1:")
#     print("to transfer press 2:")
#     print("to sidplay press 3:")
#     option = input("select option:")
#
#     if option=="1":
#         var = "c"+str(i)
#         var.create_customer()
#
#
#     if option=="2":
#         amount = int(input("enter desired transfer amount:"))
#         cr = input("enter ID of credited customer:")
#         db = input("enter ID of debit customer")
#         credit_to(cr, amount):
#         debit_to(db, amount):


c1 = Customer()
c2 = Customer()

c1.create_customer()
c2.create_customer()

c1.debit_from(100)
c2.credit_to(100)

c1.display_all()
c2.display_all()