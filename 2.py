from tkinter import *
import time

# Створення головного вікна
root = Tk()
root.title("Анімація")
canvas = Canvas(root, height=600, width=1600, bg='black')
canvas.pack()

img = PhotoImage(file='авто.png')
move1 = canvas.create_image(10, 100, image=img, anchor=NW)
canvas.image = img

# Анімація переміщення зліва направо
for i in range(1, 100):
    canvas.move(move1, 5, 0)
    root.update()
    time.sleep(0.02)

root.mainloop()

