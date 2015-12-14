from tkinter import *

master = Tk()

w = Canvas(master, width=500, height=500)
w.pack()


n = 0
k = 0
j = 0

w.create_rectangle(0, 0, 160, 160, fill="#ffffff")

while j < 8:
	i = 0
	if j % 2 == 0:
		n = 20
	else:
		n = 0
	while i < 4:
		w.create_rectangle(n, k, 20+n, 20+k, fill="#000000")
		n += 40
		i += 1
	k += 20
	n += 20
	j += 1
 
mainloop()
