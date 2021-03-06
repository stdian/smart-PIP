
from tkinter import *
import threading
import platform
import time
import sys
import os

root = None
setup = None
text = None
text2 = None

#libraries
main = ['Wheel', 'buildozer', 'cx_Freeze', 'ezprint', 'fleep', 'functools', 'pillow', 'pkgutil', 'pyautogui', 'pygame', 'setuptools', 'twine']
math = ['altair', 'jupyter', 'numpy', 'scipy', 'scrapy', 'simpy']
data = ['arrow', 'cycler', 'matplotlib', 'openpyxl', 'pandas', 'plotly', 'prettytable']
web = ['beautifulsoup4', 'cherrypy', 'cssselect', 'email', 'lxml', 'mailbox', 'paramiko', 'parsel', 'pyTelegramBotAPI', 'pyramid', 'python-simplexml', 'rdplib', 'requests', 'wget']
django = ['django', 'jinja']
kivy = ['kivy', 'kivy.deps.angle', 'kivy.deps.glew', 'kivy.deps.gstreamer', 'kivy.deps.sdl2', 'kivy_examples']
gui = ['wxPython']
databases = ['mysqlclient', 'pyodbc', 'pypyodbc', 'sqlalchemy']
console = ['argparse', 'colorama', 'termcolor']
other = ['botocore', 'conf', 'cryptography', 'psutil', 'pygments']

libraries = [main, math, data, web, django, kivy, gui, databases, console, other]
variables = []


def update_pip():
	os.system('python -m pip install --upgrade pip')


def install_window():
	global text
	global text2
	global setup

	setup = Tk()
	setup.title('Installing libraries')
	setup.geometry('400x125')
	setup.resizable(0, 0)
	setup.config(bg = '#C8C8C8')

	text = Label(setup, text = 'Please wait')
	text.config(font = ('Consolas', 15, 'bold'), bg = '#C8C8C8', height = 2)

	text2 = Label(setup, text = 'Updating pip')
	text2.config(font = ('Consolas', 15, 'bold'), bg = '#C8C8C8', height = 2)

	text2.pack()
	text.pack()


	setup.mainloop()


def install():
	global text
	global text2
	global setup

	root.destroy()
	for_install = []

	for var in variables:
		if var.get() == 1:
			for lib in libraries[variables.index(var)]:
				for_install.append(lib)

	window_thread = threading.Thread(target=install_window)
	window_thread.start()

	update_pip()

	for lib in for_install:
		text.config(text = 'Installing ' + lib)
		text2.config(text = str(for_install.index(lib) + 1) + ' / ' + str(len(for_install)))
		os.system('pip3 install ' + lib + ' --no-cache-dir --upgrade')

	text2.config(text = 'All libraries was')
	text.config(text = 'successfully install')

	window_thread.join()


def main():
	global variables
	global root

	root = Tk()

	for i in range(len(libraries)):
		variables.append(IntVar())

	root.title('Smart pip')
	root.resizable(0, 0)
	root.config(bg = '#C8C8C8')

	name = Label(root, text="Smart pip")
	name.config(font = ('Consolas', 20, 'bold'), width = 13, bg = '#C8C8C8')
	name.pack()

	checkbutton1 = Checkbutton(root, text="Main", variable=variables[0])
	checkbutton1.config(font = ('Consolas', 15, 'bold'), bg = '#C8C8C8')
	checkbutton1.pack()

	checkbutton2 = Checkbutton(root, text="Math", variable=variables[1])
	checkbutton2.config(font = ('Consolas', 15, 'bold'), height = 1, bg = '#C8C8C8')
	checkbutton2.pack()

	checkbutton3 = Checkbutton(root, text="Data", variable=variables[2])
	checkbutton3.config(font = ('Consolas', 15, 'bold'), height = 1, bg = '#C8C8C8')
	checkbutton3.pack()

	checkbutton4 = Checkbutton(root, text="Web", variable=variables[3])
	checkbutton4.config(font = ('Consolas', 15, 'bold'), height = 1, bg = '#C8C8C8')
	checkbutton4.pack()

	checkbutton5 = Checkbutton(root, text="Django", variable=variables[4])
	checkbutton5.config(font = ('Consolas', 15, 'bold'), height = 1, bg = '#C8C8C8')
	checkbutton5.pack()

	checkbutton6 = Checkbutton(root, text="Kivy", variable=variables[5])
	checkbutton6.config(font = ('Consolas', 15, 'bold'), height = 1, bg = '#C8C8C8')
	checkbutton6.pack()

	checkbutton7 = Checkbutton(root, text="GUI", variable=variables[6])
	checkbutton7.config(font = ('Consolas', 15, 'bold'), height = 1, bg = '#C8C8C8')
	checkbutton7.pack()

	checkbutton8 = Checkbutton(root, text="DataBases", variable=variables[7])
	checkbutton8.config(font = ('Consolas', 15, 'bold'), height = 1, bg = '#C8C8C8')
	checkbutton8.pack()

	checkbutton9 = Checkbutton(root, text="Console", variable=variables[8])
	checkbutton9.config(font = ('Consolas', 15, 'bold'), height = 1, bg = '#C8C8C8')
	checkbutton9.pack()

	checkbutton10 = Checkbutton(root, text="Other", variable=variables[9])
	checkbutton10.config(font = ('Consolas', 15, 'bold'), height = 1, bg = '#C8C8C8')
	checkbutton10.pack()

	button = Button(root, text="Install", command=install)
	button.config(font = ('Consolas', 20, 'bold'), width = 13)
	button.pack()

	root.mainloop()


if __name__ == '__main__':
	main()