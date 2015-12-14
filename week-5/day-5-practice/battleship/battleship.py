from tkinter import *
	

def draw_area():
	master = Tk()

	w = Canvas(master, width=550, height=550)
	w.pack()

	#def draw_line(x,y,x1,y1,array):
	#	for i in range (1,array):
	#		w.create_line(x,y,x1,y1)
	#		b += 1
	#
	#draw_line(0,b,550,b,3)
	#draw_line(b,0,b,550,3)

	a = 0
	b = 49
	for i in range (1,3):
		w.create_line(0, b, 550, b)
		w.create_line(b, 0, b, 550)
		b += 1

	for i in range(1, 11):
		w.create_line(0, 50+a, 550, 50+a)
		w.create_line(50+a, 0, 50+a, 550)
		a += 50

	abc = 'ABCDEFGHIL'
	a = 0
	i = 0

	for n in abc:
		w.create_text(75+a,25,font="Times 20 bold", text= abc[i])
		w.create_text(25, 75+a, font="Times 20 bold", text= str(i+1))
		a += 50
		i += 1

	mainloop()
draw_area()
