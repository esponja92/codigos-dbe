#!-*- coding: utf8 -*-
import Tkinter
from Tkinter import *
from ScrolledText import *
import tkFileDialog
import tkMessageBox
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

root = Tkinter.Tk(className="pyBoni++")
root.geometry('640x480')
textPad = ScrolledText(root, width=640, height=480) #cria a area de texto
filename = ''

def new_command():
	textPad.delete('1.0',END)
	global filename
	filename = ''

def open_command():
	file = tkFileDialog.askopenfile(parent=root, mode='rb', title='Selecione um arquivo',filetypes=[('all files', '.*'), ('text files', '.txt')])
	if file != None:
		global filename
		filename = file.name
		contents = file.read()
		textPad.insert('1.0',contents)
		file.close()

def save_command():
	if filename == '':
		save_as_command()
	else:
		file = open(filename, 'w')
		if file != None:
			data = textPad.get('1.0',END+'-1c')
			file.write(data)
			file.close()

def save_as_command():
	file = tkFileDialog.asksaveasfile(mode='w', filetypes=[('all files', '.*'), ('text files', '.txt')], defaultextension=".txt")
	if file != None:
		data = textPad.get('1.0',END+'-1c')
		file.write(data)
		file.close()

def exit_command():
	ok = tkMessageBox.askokcancel("Sair", "Você realmente deseja sair?\nTodas as modificações não serão salvas.")
	if ok:
		root.destroy()

def about_command():
	label = tkMessageBox.showinfo("Sobre", "pyBoni++ \nCopyright (c) Hugo Dantas 2017")

menu = Menu(root)

root.config(menu=menu)


filemenu = Menu(menu)

menu.add_cascade(label="Arquivo", menu=filemenu)
filemenu.add_command(label="Novo", command=new_command)
filemenu.add_command(label="Abrir...", command=open_command)
filemenu.add_command(label="Salvar", command=save_command)
filemenu.add_command(label="Salvar como...", command=save_as_command)
filemenu.add_separator()
filemenu.add_command(label="Sair", command=exit_command)

helpmenu = Menu(menu)
menu.add_cascade(label="Ajuda", menu=helpmenu)
helpmenu.add_command(label="Sobre", command=about_command)

textPad.pack()
root.mainloop()