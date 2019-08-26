from tkinter import *
from tkinter import ttk


root = Tk()
root.title('Finding Palindrome')



sourceNum = StringVar()
PalindromeNumber = StringVar()
loopingNumber = StringVar()

def twist(twistnum):
	twistnum = int(str(twistnum)[::-1])
	return twistnum

def sum(num):
	num = int(num) + int(twist(num))
	return num

def looping(*args):
	Palindrome = False
	loop = 0
	PalindromeNum = int(sourceNum.get())
	while Palindrome == False:
		if PalindromeNum == twist(PalindromeNum):
			Palindrome = True
			PalindromeNumber.set(PalindromeNum)
			loopingNumber.set(loop)
		else:
			PalindromeNum = sum(PalindromeNum)
			loop += 1
			if loop > 1000:
				PalindromeNumber.set("error")
				loopingNumber.set("error")
				break

mainframe = ttk.Frame(root)
mainframe.grid(column = 0, row = 0)

ttk.Label(mainframe, text = 'Your number').grid(column = 0, row = 0)
entry = ttk.Entry(mainframe, textvariable = sourceNum, width = 5)
entry.grid(column = 1, row = 0)
ttk.Label(mainframe, text = 'became polindrome after ').grid(column = 2, row = 0)
ttk.Label(mainframe, textvariable = loopingNumber).grid(column = 3, row = 0)
ttk.Label(mainframe, text = 'iteration.').grid(column = 4, row = 0)

ttk.Label(mainframe, text = 'And polindrome is equals ').grid(column = 2, row = 1)
ttk.Label(mainframe, textvariable = PalindromeNumber).grid(column = 3, row = 1)

ttk.Button(mainframe, command = looping, text = 'calculate').grid(column = 3, row = 2)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

entry.focus()
root.bind('<Return>', looping)

root.mainloop()
