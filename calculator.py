

#Task 2 :CALCULATOR

from tkinter import *
expression = ""

def press(num):

	global expression
	expression = expression + str(num)
	equation.set(expression)

def equalpress():

	try:

		global expression
		total = str(eval(expression))
		equation.set(total)
		expression = ""

	except:

		equation.set(" error ")
		expression = ""

def clear():

	global expression
	expression = ""
	equation.set("")

if __name__ == "__main__":

	gui = Tk()
	gui.configure(background="black")
	gui.title("Calculator")
	gui.geometry("420x590+120+160")
	gui.resizable(False,False)
	gui.configure(bg="black")

	equation = StringVar()
	field = Entry(gui, textvariable=equation,bg=("white"),font="arial 28")
	field.grid(column=4,padx=10,pady=20,ipadx=50,ipady=20)

	clear=Button(gui,text='c',font=("arial",30,"bold"),bd=1,fg='white',bg='#3697f5',
			  command=clear,width=3,height=1).place(x=20,y=130)
	

	divide = Button(gui, text=' / ',font=("arial",30,"bold"),bd=1, fg='white', bg='#242d36',
				  command=lambda: press("/"), height=1, width=3).place(x=120,y=130)
	

	module = Button(gui, text=' % ',font=("arial",30,"bold"),bd=1, fg='white', bg='#242d36',
					command=lambda:press("%"), height=1, width=3).place(x=220,y=130)
	

	multiply = Button(gui, text=' * ',font=("arial",30,"bold"),bd=1, fg='white', bg='#242d36',
					command=lambda: press("*"), height=1, width=3).place(x=320,y=130)


	button1 = Button(gui, text=' 7 ', font=("arial",30,"bold"),bd=1,fg='white', bg='#242d36',
					command=lambda: press("7"), height=1, width=3).place(x=20,y=220)
	

	button2 = Button(gui, text=' 8 ',font=("arial",30,"bold"),bd=1, fg='white', bg='#242d36',
					command=lambda: press("8"), height=1, width=3).place(x=120,y=220)
	

	button3 = Button(gui, text=' 9 ',font=("arial",30,"bold"),bd=1, fg='white', bg='#242d36',
					command=lambda: press("9"), height=1, width=3).place(x=220,y=220)
	

	minus= Button(gui, text=' - ',font=("arial",30,"bold"),bd=1, fg='white', bg='#242d36',
					command=lambda: press("-"), height=1, width=3).place(x=320,y=220)
	

	button4 = Button(gui, text=' 4',font=("arial",30,"bold"),bd=1, fg='white', bg='#242d36',
					command=lambda: press("4"), height=1, width=3).place(x=20,y=310)
	
	button5 = Button(gui, text=' 5',font=("arial",30,"bold"),bd=1, fg='white', bg='#242d36',
					command=lambda: press("5"), height=1, width=3).place(x=120,y=310)
	
	button6 = Button(gui, text=' 6',font=("arial",30,"bold"),bd=1, fg='white', bg='#242d36',
					command=lambda: press("6"), height=1, width=3).place(x=220,y=310)
	
	plus= Button(gui, text=' +',font=("arial",30,"bold"),bd=1, fg='white', bg='#242d36',
					command=lambda: press("+"), height=1, width=3).place(x=320,y=310)
	

	button7 = Button(gui, text=' 1',font=("arial",30,"bold"),bd=1, fg='white', bg='#242d36',
					command=lambda: press("1"), height=1, width=3).place(x=20,y=400)

	button8 = Button(gui, text=' 2',font=("arial",30,"bold"),bd=1, fg='white', bg='#242d36',
				command=lambda: press("2"), height=1, width=3).place(x=120,y=400)
	
	button9 = Button(gui, text=' 3',font=("arial",30,"bold"),bd=1, fg='white', bg='#242d36',
				command=lambda: press("3"), height=1, width=3).place(x=220,y=400)

	button = Button(gui, text=' 0',font=("arial",30,"bold"),bd=1, fg='white', bg='#242d36',
				command=lambda: press("0"), height=1, width=7).place(x=20,y=490)
	
	button = Button(gui, text=' .',font=("arial",30,"bold"),bd=1, fg='white', bg='#242d36',
				command=lambda: press("."), height=1, width=3).place(x=220,y=490)
	
	equal =Button(gui, text=' = ',font=("arial",30,"bold"),bd=1, fg='white', bg='#242d36',
				command=equalpress, height=3, width=3).place(x=320,y=400)
	
	
	gui.mainloop()