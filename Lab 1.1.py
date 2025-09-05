while True:
    print ("1. addition")
    print ("2. subtraction")
    print ("3. multiplication")
    print ("4. division")
    print ("5. quit")
    option = input("select an option")

    if option =="1":
        n1 = int(input("first number:"))
        n2 = int(input("second number:"))
        print("the answer is", n1+n2)
    elif option =="2":
        n1 = int(input("first number:"))
        n2 = int(input("second number:"))
        print("the answer is", n1-n2)
    elif option =="3":
        n1 = int(input("first number:"))
        n2 = int(input("second number:"))
        print("the answer is", n1*n2)
    elif option =="4":
        n1 = int(input("first number:"))
        n2 = int(input("second number:"))
        print("the answer is", n1/n2)
    elif option =="5":
        break