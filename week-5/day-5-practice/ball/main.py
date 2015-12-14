from tkinter import *
from ball import Ball


master = Tk()

canvas = Canvas(master, width= 500, height=500)
canvas.pack()

ball = Ball((200,200),(-1, 1), 20)

while True:
	ball.move()
	bbox = ball.get_bbox()
	canvas.create_rectangle(0, 0, 500, 500, fill='#ffffff')
	canvas.create_oval(bbox, fill='#ff0000')
	canvas.after(1000 // 60)
	canvas.update()

mainloop()
