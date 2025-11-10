#create a menu with three buttons
#create q, en q, de q, and display
import tkinter
class Queue:
    def __init__(self):
        self.element = []
    def enqueue(self):
        self.element.append(input("enter value"))
    def dequeue(self):
        self.element.remove(0)
    def displayqueue(self):
        print("Elements ub queue:")
        for i in self.element:
            print(i)

root = tkinter.Tk()
root.resizable(False, False)
myCanvas = tkinter.Canvas(root, bg="black", height=600, width=800)
q1 = Queue
#createq = tkinter.Button(root, text="Create Queue", command= fg="white")


addq = tkinter.Button(root, text="En Queue", command=q1.enqueue(), fg="white")


removeq= tkinter.Button(root, text="De Queue", command=q1.dequeue(), fg="white")


disp = tkinter.Button(root, text="Display", command=q1.displayqueue(), fg="white")

#main code

