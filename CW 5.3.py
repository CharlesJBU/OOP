myQueue=[]
def enq():
    v =input("enter name to place in queue:")
    myQueue.append(v)
def deq():
    v =input("enter name to dequeue:")
    myQueue.remove(v)
def dis():
    print(myQueue)
#maincode----------
while 1:
    print("press 1 to enqueue:")
    print("press 2 to dequeue:")
    print("press 3 to display:")
    print("press 4 to quit:")
    option = input("enter desired function:")

    if option =="1":
        enq()
    if option =="2":
        deq()
    if option =="3":
        dis()
    if option =="4":
        exit(0)