def area_rectangle():
    a = int(input("enter length:"))
    b = int(input("enter breadth"))
    print(a*b)
def vol_cube():
    a = int(input("enter length"))
    b = int(input("enter breadth"))
    c = int(input("enter height"))
    print(a*b*c)
def area_circle():
    r = int(input("enter radius"))
    print(3.14*r*r)
def vol_circle():
    r = int(input("enter radius"))
    print(2*3.14*r)

#main code-------------------
while 1:
    print("press 1 to find area of rectangle:")
    print("press 2 to find the volume of a cube:")
    print("press 3 to find the area of a circle:")
    print("press 4 to find the volume of a circle:")
    print("press 5 to quit:")
    option =input("enter desired function:")
    if option =="1":
        area_rectangle()
    if option =="2":
        vol_cube()
    if option =="3":
        area_circle()
    if option =="4":
        vol_circle()
    if option =="5":
        exit(0)