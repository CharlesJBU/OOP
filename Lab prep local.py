myStudents = {}

while 1:
    print("press 1 to update list")
    print("press 2 to delete list")
    print("press 3 to edit list")
    print("press 4 to print list")
    print("press 5 to quit")
    option = input("select action:")
    if option =="1":
        sid = input("enter student ID")
        nname = input("enter name:")
        mmajor = input("enter student major:")
        yyear = input("enter student year:")
        tcredits = input("enter student credits:")
        ggpa = input("enter student gpa:")
        myStudents.update({sid:{"name":nname, "major":mmajor, "year":yyear, "credits":tcredits, "gpa":ggpa}})
    if option =="2":
        sid = input("enter student id:")
        del myStudents[sid]
    if option =="3":
        sid = input("enter student ID")
        nname = input("enter name:")
        mmajor = input("enter student major:")
        yyear = input("enter student year:")
        tcredits = input("enter student credits:")
        ggpa = input("enter student gpa:")
        myStudents.update({sid: {"name": nname, "major": mmajor, "year": yyear, "credits": tcredits, "gpa": ggpa}})
    if option =="4":
        print(myStudents)
    if option =="5":
        exit(0)