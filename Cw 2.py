stu_name = input("enter the student name:")

course1 = int(input("enter the grade points for course 1:"))
course2 = int(input("enter the grade points for course 1:"))
course3 = int(input("enter the grade points for course 1:"))
course4 = int(input("enter the grade points for course 1:"))
course5 = int(input("enter the grade points for course 1:"))

total = course1+course2+course3+course4+course5
print("The Total is:", total)

total_percentage = ((total/500)*100)

if total_percentage <100 and total_percentage >90:
    print ("grade A:")
elif total_percentage <89 and total_percentage>80:
    print ("grade B:")
elif total_percentage <79 and total_percentage>70:
    print ("grade C:")
elif total_percentage <69 and total_percentage>60:
    print ("grade D:")
else:
    print ("grade F:")