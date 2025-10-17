Database = {}

while 1:
    print("Press 1 to log in:")
    print("Press 2 to create an account:")
    print("Press 3 to exit:")
    option = input("Enter command:")
    if option =="1":
        uid = input("input user ID")
        pwd = input("enter password:")


    if option =="2":
        uid = input("enter user ID:")
        nname = input("Enter full name:")
        pwd: input("Enter password:"))
        cclass = input("enter hospital role:")
        print("account created successfully! Proceed to log in.")

    Database.update({uid:{"name":nname, "password":pwd}})
        print(Database)
