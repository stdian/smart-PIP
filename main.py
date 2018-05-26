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


root = Tk()
variables = []
for i in range(len(libraries)):
	variables.append(IntVar())
print(variables)

var2 = IntVar()
var3 = IntVar()

checkbutton1 = Checkbutton(root, text="Main", variable=variables[0])
checkbutton1.pack()
checkbutton2 = Checkbutton(root, text="Math", variable=variables[1])
checkbutton2.pack()
checkbutton3 = Checkbutton(root, text="Data", variable=variables[2])
checkbutton3.pack()

root.mainloop()


