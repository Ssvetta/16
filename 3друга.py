from tkinter import *

root = Tk()
root.title("Нічне місто")

canvas_width = 800
canvas_height = 600
canvas = Canvas(root, width=canvas_width, height=canvas_height, bg="midnightblue")
canvas.pack()

#Елементи нічного неба

#Місяць
moon_center_x = 650
moon_center_y = 100
moon_radius = 60
canvas.create_oval(moon_center_x - moon_radius, moon_center_y - moon_radius,
                   moon_center_x + moon_radius, moon_center_y + moon_radius,
                   fill="lightgray", outline="gray")
# Частина, що шукає місяць, щоб зробити півмісяць
canvas.create_oval(moon_center_x - moon_radius + 20, moon_center_y - moon_radius,
                   moon_center_x + moon_radius + 20, moon_center_y + moon_radius,
                   fill="midnightblue", outline="midnightblue")


# Зірки
def create_star(x, y, size=3, color="white"):
    canvas.create_oval(x - size, y - size, x + size, y + size, fill=color, outline=color)

create_star(50, 50)
create_star(120, 80, size=2)
create_star(200, 30)
create_star(300, 70, size=4)
create_star(400, 100, size=2)
create_star(700, 40)
create_star(580, 20, size=3)
create_star(450, 150)
create_star(350, 120, size=2)
create_star(250, 180, size=3)


#Силуети будівель (різної висоти та ширини)

# Горизонт
horizon_y = canvas_height - 150

# Будівля 1
canvas.create_rectangle(50, horizon_y - 150, 150, horizon_y, fill="darkslategray", outline="black")
canvas.create_rectangle(65, horizon_y - 130, 80, horizon_y - 110, fill="yellow") # Вікно
canvas.create_rectangle(90, horizon_y - 130, 105, horizon_y - 110, fill="yellow") # Вікно
canvas.create_rectangle(65, horizon_y - 90, 80, horizon_y - 70, fill="yellow") # Вікно

# Будівля 2 (вища)
canvas.create_rectangle(180, horizon_y - 250, 250, horizon_y, fill="gray", outline="black")
canvas.create_rectangle(195, horizon_y - 230, 210, horizon_y - 210, fill="yellow")
canvas.create_rectangle(220, horizon_y - 230, 235, horizon_y - 210, fill="yellow")
canvas.create_rectangle(195, horizon_y - 180, 210, horizon_y - 160, fill="yellow")
canvas.create_rectangle(220, horizon_y - 180, 235, horizon_y - 160, fill="yellow")

# Будівля 3 (ширша)
canvas.create_rectangle(280, horizon_y - 100, 400, horizon_y, fill="dimgray", outline="black")
canvas.create_rectangle(290, horizon_y - 80, 310, horizon_y - 60, fill="yellow")
canvas.create_rectangle(320, horizon_y - 80, 340, horizon_y - 60, fill="yellow")
canvas.create_rectangle(350, horizon_y - 80, 370, horizon_y - 60, fill="yellow")


# Будівля 4 (ззаду, темніша)
canvas.create_rectangle(430, horizon_y - 180, 500, horizon_y, fill="darkslategray", outline="black")
canvas.create_rectangle(440, horizon_y - 160, 455, horizon_y - 140, fill="yellow")
canvas.create_rectangle(465, horizon_y - 160, 480, horizon_y - 140, fill="yellow")


# Будівля 5 (праворуч, вища)
canvas.create_rectangle(530, horizon_y - 220, 600, horizon_y, fill="gray", outline="black")
canvas.create_rectangle(540, horizon_y - 200, 555, horizon_y - 180, fill="yellow")
canvas.create_rectangle(565, horizon_y - 200, 580, horizon_y - 180, fill="yellow")
canvas.create_rectangle(540, horizon_y - 150, 555, horizon_y - 130, fill="yellow")
canvas.create_rectangle(565, horizon_y - 150, 580, horizon_y - 130, fill="yellow")


# Дорога на передньому плані
canvas.create_rectangle(0, horizon_y, canvas_width, canvas_height, fill="black", outline="black")

root.mainloop()
