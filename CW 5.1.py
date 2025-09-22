project ={}

while 1:
    print("press 1 for project initiation:")
    print("press 2 for project closure:")
    print("press 3 for project progress update:")
    print("press 4 to print a specific project:")
    print("press 5 to print all projects:")
    print("press 6 to quit application:")
    option = int(input("Input desired action:"))

    if option =="1":
        manager = []
        tech = []
        team = []
        pid = input("input project ID:")
        ptitle = input("input project title:")
        m = int(input("how many managers would you like to enter:"))
        for i in range(0,m):
            managers.append(input("enter managers name:"))
        sdate = input("input start date:")
        edate = input("input end date:")
        ssponsor = input("input sponsor:")
        bbudget = input("input sponsor:")
        ttech = input("input technology used:")
        for i in range
        tmembers = input("input team members:")
        project.update({pid:{
                        "project title":ptitle,
                        "start date":sdate,
                        "end date":edate,
                        "sponsor":ssponsor,
                        "budget":bbudget,
                        "technology used":ttech,
                        "team membsers":tmembers}})

    if option =="2":
        ddelete = input("input project ID to delete:")
        del project[ddelete]
        print(project)
    if option =="3":
        pid = input("input project ID:")
        ptitle = input("input project title:")
        sdate = input("input start date:")
        edate = input("input end date:")
        ssponsor = input("input sponsor:")
        bbudget = input("input sponsor:")
        ttech = input("input technology used:")
        tmembers = input("input team members:")
        project.update({pid:{
                        "project title":ptitle,
                        "start date":sdate,
                        "end date":edate,
                        "sponsor":ssponsor,
                        "budget":bbudget,
                        "technology used":ttech,
                        "team membsers":tmembers}})

    if option =="4":
        ppid = input("desired project to print:")
        print(project(pid))
    if option =="5":
        print(project)

    if option =="6":
        exit(0)