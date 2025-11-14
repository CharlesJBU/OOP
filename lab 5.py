import tkinter as tk
from tkinter import simpledialog, messagebox

stack = []
queue = []

def add_to_queue():
    item = simpledialog.askstring("Add to Queue", "Enter item to enqueue:")
    queue.append(item)
    messagebox.showinfo("Added to queue.")

def remove_from_queue():
    queue.remove(queue[0])
    messagebox.showinfo("Removed from queue.")

def display_queue():
    messagebox.showinfo("Current queue", f"{queue}")

def add_to_top():
    item = simpledialog.askstring("Add to Stack", "Enter item:")
    stack.push(item)
    messagebox.showinfo("Added to top of stack.")

def remove_from_stack():
    stack.pop()
    messagebox.showinfo("Removed from top of stack.")

def display_stack():
    messagebox.showinfo("Current stack", f"\n{items}")

root = tk.Tk()
root.title("Stack + Queue builder")

tk.Button(root, text="Add to Queue", width=30, command=add_to_queue).pack(pady=5)
tk.Button(root, text="Remove from Queue", width=30, command=remove_from_queue).pack(pady=5)
tk.Button(root, text="Display Queue", width=30, command=display_queue).pack(pady=5)

tk.Button(root, text="Add to Top", width=30, command=add_to_top).pack(pady=5)
tk.Button(root, text="Remove from Stack", width=30, command=remove_from_stack).pack(pady=5)
tk.Button(root, text="Display Stack", width=30, command=display_stack).pack(pady=5)

root.mainloop()