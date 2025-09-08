myList = []

while 1:
    print("1: Append to the list:")
    print("2: Remove from the list:")
    print("3: pop from list:")
    print("4: display the list:")
    print("5: quit:")
    option = input("select an option:")
    if option =="1":
        n1 = input("enter month:")
        myList.append(n1)
        print(myList)
    if option =="2":
        n2 = input("remove month:")
        myList.remove(n2)

