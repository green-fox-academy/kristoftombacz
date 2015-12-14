from tkinter import *

master = Tk()

w = Canvas(master, width=500, height=500)
w.pack()

#a = 0
#b = 0
#for i in range(1,500):
#	w.create_line(a, 0, 0, b, fill= "#2223e5")
#	a += 3
#	b += 3

#for i in range(1,500):
#	w.create_oval(200, 200, 300, 300, fill = "#ff0000")


#w.create_line(250, 0, 250, 500, fill="green")
#w.create_line(0, 250, 500, 250, fill="green")
#w.create_line(0, 0, 500, 500, fill="green")
#w.create_line(0, 500, 500, 0, fill="green")

a = 0
for i in range(1, 100):
	w.create_line(0, 0, a, 500, fill="yellow")
	a += 5 

a = 0
for i in range(1, 100):
	w.create_line(500, 500, 500-a, 0, fill="blue")
	a += 5

a = 0
for i in range(1, 100):
	w.create_line(0, 500, 250+a, 250+a, fill="red")
	a += 5
a = 0
for i in range(1, 100):
	w.create_line(500, 0, 250-a, 250-a, fill="green")
	a += 5

mainloop()
