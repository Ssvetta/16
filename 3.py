from tkinter import *
root = Tk()
root.title("Малювання фігур")
canvas = Canvas(root, width=400, height=300, bg='white')
canvas.pack()
canvas.create_oval(50, 50, 150, 150, fill='skyblue', outline='black')
canvas.create_polygon(250, 150, 200, 50, 300, 50, fill='pink', outline='black')
root.mainloop()
