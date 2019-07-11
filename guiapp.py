#!/usr/bin/python3

#===========================================================
#
# Python GUI Appication
#
# Python3 OS:Windows or Linux
#
# Date       Version Name    Comment
# 2019/07/11 0.00    Hantani New
#
#===========================================================

import tkinter as tk
from tkinter import Menu
from tkinter import messagebox
from tkinter.font import Font
from tkinter import filedialog as tkFileDialog

class GuiApp:

    def __init__(self):
        self.version = "Ver0.00"
        self.title="Paramater Checker"
        self.main()

    def main(self):
        self.init()
        self.root.mainloop()

    def init(self):
        self.root = tk.Tk()
        self.root.title(self.title)
        #Menu
        menu_bar = Menu(self.root)
        self.root.config(menu = menu_bar)
    
        file_menu = Menu(menu_bar,tearoff=0)
        file_menu.add_command(label="New",command = lambda:self.menu_new())
        file_menu.add_command(label="Clear",command = lambda:self.menu_clear())
        file_menu.add_separator()
        file_menu.add_command(label="Exit",command = lambda:self.myExit())
        menu_bar.add_cascade(label="Files",menu=file_menu)

        opt_menu = Menu(menu_bar,tearoff=0)
        opt_menu.add_command(label="Debug On",command = lambda:self.menu_option1())
        opt_menu.add_separator()
        opt_menu.add_command(label="Debug Off",command = lambda:self.menu_option2())
        menu_bar.add_cascade(label="Options",menu=opt_menu)

        help_menu = Menu(menu_bar,tearoff=0)
        help_menu.add_command(label="Help",command = lambda:self.menu_help())
        menu_bar.add_cascade(label="Help",menu=help_menu)


        #window
        self.root.minsize(100, 100)
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        # Frame
        frame1 = tk.Frame(self.root)
        frame1.rowconfigure(0, weight=1)
        frame1.columnconfigure(0, weight=1)
        frame1.grid(sticky=(tk.N,tk.W,tk.S,tk.E))
    
        ##Button
        #button1 = tk.Button(frame1, text='OK', command=self.button_click)
        #button1.grid(row=0, column=0, columnspan=2, sticky=(tk.N,tk.E))
    
        # Text
        f = Font(family='Helvetica', size=11)
        self.txt = tk.Text(frame1)
        self.txt.configure(font=f)
        self.txt.insert(1.0, "[START]\n")
        #self.txt.grid(row=1, column=0, sticky=(tk.N,tk.W,tk.S,tk.E))
        self.txt.grid(row=0, column=0, sticky=(tk.N,tk.W,tk.S,tk.E))
    
         # Scrollbar
        scrollbar = tk.Scrollbar(
            frame1, 
            orient=tk.VERTICAL, 
            command=self.txt.yview)
        self.txt['yscrollcommand'] = scrollbar.set
        #scrollbar.grid(row=1,column=1,sticky=(tk.N,tk.S))
        scrollbar.grid(row=0,column=1,sticky=(tk.N,tk.S))

    def myExit(self):
        self.root.quit()
        exit()

    def button_click(self):
        messagebox.showinfo("title","message")
        self.txt.insert(tk.END,"message\n")

    def menu_new(self):
        self.file_select()

    def menu_clear(self):
        self.txt.delete(1.0,tk.END)

    def menu_option1(self):
        self.myDebug = True
        messagebox.showinfo("Debug mode","Debug ON")
        self.txt.insert(tk.END,"Debug ON\n")

    def menu_option2(self):
        self.myDebug = False
        messagebox.showinfo("Debug mode","Debug OFF")
        self.txt.insert(tk.END,"Debug OFF\n")
        
    def menu_help(self):
        help_message = self.title + " " + self.version
        self.txt.insert(tk.END,"\n" + help_message + "\n")

    def file_select(self):
        fTyp=[('テキストファイル','*.txt')]
        #複数のタイプを指定することも可能。

        iDir='/home/ユーザ名/'  #iDir='c:/' #Windows

        #askopenfilename 一つのファイルを選択する。
        filename=tkFileDialog.askopenfilename(filetypes=fTyp,initialdir=iDir) 

        messagebox.showinfo('FILE NAME is ...',filename)
        self.filename = filename
        self.logPrintln('FILE NAME is ' + filename + '\n')
        #self.dbgPrintln(self.version)

    def logPrint(sefl,str):
        self.txt.insert(tk.END,str)
        
    def logPrintln(sefl,str):
        self.logPrint(str + "\n")

    def dbgPrint(sefl,str):
        if self.myDebug == True:
            self.logPrint(str)
        
    def dbgPrintln(sefl,str):
        self.dbgPrint(str + "\n")

if __name__ == "__main__":
    ga = GuiApp()
