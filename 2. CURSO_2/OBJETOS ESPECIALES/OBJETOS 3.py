from tkinter import *
from tkinter import tix

class Window:

    def __init__(self, root):

        self.labelList = []
        self.notebook = tix.NoteBook(root, ipadx=3, ipady=3) 
        self.notebook.add('sheet_1', label="Sheet 1", underline=0) 
        self.notebook.add('sheet_2', label="Sheet 2", underline=0)
        self.notebook.add('sheet_3', label="Sheet 3", underline=0)
        self.notebook.pack()
        #self.notebook.grid(row=0, column=0)

        tab1=self.notebook.sheet_1
        tab2=self.notebook.sheet_2
        tab3=self.notebook.sheet_3



        self.myMainContainer = Frame(tab1)
        self.myMainContainer.pack()
        #self.myMainContainer.grid(row=0, column=0)

        scrwin = tix.ScrolledWindow(self.myMainContainer, scrollbar='y') 
        scrwin.pack()
        #scrwin.grid(row=0, column=0) 
        self.win = scrwin.window


        for i in range (20):
            self.labelList.append((Label(self.win)))
            self.labelList[-1].config(text= "Bla", relief = SUNKEN)
            self.labelList[-1].grid(row=i, column=0, sticky=W+E)

root = tix.Tk()
myWindow = Window(root)

root.mainloop()