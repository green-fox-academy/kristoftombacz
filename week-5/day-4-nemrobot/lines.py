from tkinter import *

master = Tk()

w = Canvas(master, width=500, height=500)
w.pack()

for i in range(1, 500, 10):
	n = i
	k = 500 - i
	w.create_line(n, 0, 0, k, fill = "#0f0f0f")

for i in range(1, 500, 20):
	n = 500 + i
	k = 800 - i
	w.create_line(n, 0, 0, k, fill = "red")

mainloop()

