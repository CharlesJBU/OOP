#shape makin
import tkinter

root = tkinter.Tk()
root.resizable(False,False)

#create canvas

myCanvas = tkinter.Canvas(root, bg="white", height=500, width=800)

shape1 = myCanvas.create_oval(0,50,100,100, fill="blue")

shape2 = myCanvas.create_rectangle(230, 10, 290, 60, fill="red")

shape3 = myCanvas.create_arc(30,200, 90, 100, start=0, extent=210, fill="green")

myCanvas.pack()
root.mainloop()