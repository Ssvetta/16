from tkinter import*
import winsound
from PIL import Image, ImageTk
def play():
    if var.get() == 0:
        winsound.PlaySound("9.wav", winsound.SND_FILENAME)
    elif var.get() == 1:
        winsound.PlaySound("10.wav", winsound.SND_FILENAME)
    elif var.get() == 2:
        winsound.PlaySound("11.wav", winsound.SND_FILENAME)
    elif var.get() == 3:
        winsound.PlaySound("12.wav", winsound.SND_FILENAME)
    elif var.get() == 4:
        winsound.PlaySound("13.wav", winsound.SND_FILENAME)
    elif var.get() == 5:
        winsound.PlaySound("14.wav", winsound.SND_FILENAME)
    elif var.get() == 6:
        winsound.PlaySound("15.wav", winsound.SND_FILENAME)

root=Tk()
root.minsize(width=300, height=600)
root.title("Словник")
root['bg']='white'
frame = LabelFrame(root, text="Виберіть слово", padx=5, bg="white",bd=3)
frame.pack()
var = IntVar()
var.set(0)
Radiobutton1 = Radiobutton(frame,bg="white",text="Понеділок",
variable=var, value=0).pack(anchor="w")
Radiobutton2 = Radiobutton(frame,bg="white",text="Вівторок",
variable=var, value=1).pack(anchor="w")
Radiobutton3 = Radiobutton(frame,bg="white",text="Середа",
variable=var, value=2).pack(anchor="w")
Radiobutton4 = Radiobutton(frame,bg="white",text="Четвер",
variable=var, value=3).pack(anchor="w")
Radiobutton5 = Radiobutton(frame,bg="white",text="П'ятниця",
variable=var, value=4).pack(anchor="w")
Radiobutton6 = Radiobutton(frame,bg="white",text="Субота",
variable=var, value=5).pack(anchor="w")
Radiobutton7 = Radiobutton(frame,bg="white",text="Неділя",
variable=var, value=6).pack(anchor="w")

button = Button(text="Відтворити",width=15, height=2,bg="yellow",command=play).pack()
canvas = Canvas(root,width=545,height=273,bg='white')
canvas.pack()
img = Image.open('тижні.png')
img = img.resize((550, 275))
img = ImageTk.PhotoImage(img)
canvas.create_image(0, 0, image=img, anchor=NW)
canvas.image = img

root.mainloop()