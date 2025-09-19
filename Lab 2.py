myStudents = {}

while 1:
    print("press 1 to add a student")
    print("press 2 to delete student")
    print("press 3 to modify a student")
    print("press 4 display all students")
    print("press 5 exit program")
    option = input("select function:")

    if option =="1":
        sid = input("enter student ID:")
        nname = input("enter student name:")
        lab1 = int(input("enter lab 1 grade:"))
        lab2 = int(input("enter lab 2 grade:"))
        lab3 = int(input("enter lab 3 grade:"))
        lab4 = int(input("enter lab 4 grade:"))
        lab5 = int(input("enter lab 5 grade:"))
        total =(lab1+lab2+lab3+lab4+lab5)
        avg =((total/5)*10)
        myStudents.update({sid:{"name":nname, "lab 1 grade":lab1, "lab 2 grade":lab2, "lab 3 grade":lab3, "lab 4 grade":lab4, "lab 5 grade":lab5, "grade average":avg}})
    if option =="2":
        sid = input("enter student ID:")
        del myStudents[sid]
    if option =="3":
        sid = input("enter student ID:")
        nname = input("enter student name:")
        lab1 = int(input("enter lab 1 grade:"))
        lab2 = int(input("enter lab 2 grade:"))
        lab3 = int(input("enter lab 3 grade:"))
        lab4 = int(input("enter lab 4 grade:"))
        lab5 = int(input("enter lab 5 grade:"))
        total = (lab1 + lab2 + lab3 + lab4 + lab5)
        avg = ((total / 5) * 10)
        myStudents.update({sid:{"name":nname, "lab 1 grade":lab1, "lab 2 grade":lab2, "lab 3 grade":lab3, "lab 4 grade":lab4, "lab 5 grade":lab5, "grade average":avg}})
    if option =="4":
        print(myStudents)
    if option =="5":
        exit(0)
