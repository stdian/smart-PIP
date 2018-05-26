from tkinter import *

#libraries
main = ['Wheel', 'buildozer', 'ezprint', 'fleep', 'functools', 'pillow', 'pkgutil', 'pygame', 'setuptools', 'twine']
math = ['altair', 'jupyter', 'numpy', 'scipy', 'scrapy', 'simpy']
data = ['plotly', 'pandas', 'matplotlib', 'cycler', 'arrow', 'openpyxl', 'prettytable']
web = ['beautifulsoup4', 'rdplib', 'requests', 'paramiko', 'wget', 'pyTelegramBotAPI', 'lxml', 'cssselect', 'email', 'cherrypy', 'mailbox', 'parsel', 'python-simplexml', 'pyramid']
django = ['django', 'jinja']
kivy = ['kivy', 'kivy.deps.angle', 'kivy.deps.glew', 'kivy.deps.gstreamer', 'kivy.deps.sdl2', 'kivy_examples']
gui = ['turtle', 'wxPython']
databases = ['mysqlclient', 'pyodbc', 'pypyodbc', 'sqlalchemy']
console = ['argparse', 'colorama', 'termcolor']
other = ['botocore', 'conf', 'cryptography', 'psutil', 'pygments']

libraries = [main, math, data, web, django, kivy, gui, databases, console, other]



def setup():
	pass







def main():
	root = Tk()

	variables = []
	for i in range(len(libraries)):
		variables.append(IntVar())

	root.title('Smart pip')

	root.resizable(0, 0)

	name = Label(root, text="Smart pip")
	name.pack()

	checkbutton1 = Checkbutton(root, text="Main", variable=variables[0])
	checkbutton1.pack()

	checkbutton2 = Checkbutton(root, text="Math", variable=variables[1])
	checkbutton2.pack()

	checkbutton3 = Checkbutton(root, text="Data", variable=variables[2])
	checkbutton3.pack()

	checkbutton4 = Checkbutton(root, text="Web", variable=variables[3])
	checkbutton4.pack()

	checkbutton5 = Checkbutton(root, text="Django", variable=variables[4])
	checkbutton5.pack()

	checkbutton6 = Checkbutton(root, text="Kivy", variable=variables[5])
	checkbutton6.pack()

	checkbutton7 = Checkbutton(root, text="GUI", variable=variables[6])
	checkbutton7.pack()

	checkbutton8 = Checkbutton(root, text="DataBases", variable=variables[7])
	checkbutton8.pack()

	checkbutton9 = Checkbutton(root, text="Console", variable=variables[8])
	checkbutton9.pack()

	checkbutton10 = Checkbutton(root, text="Other", variable=variables[9])
	checkbutton10.pack()

	button = Button(root, text="Install", command=setup)
	button.pack()

	root.mainloop()


if __name__ == '__main__':
	main()