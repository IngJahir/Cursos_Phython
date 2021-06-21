from tkinter import tix
root = tix.Tk()

'''
tooltip = tix.Balloon(root, initwait=250)
root.title("VENTANA DE CALCULO")
root.iconbitmap("Icono.ico")
'''
swr=tix.ScrolledWindow(root)
swr.pack(fill=tix.BOTH, expand=1)

nb=tix.NoteBook(swr.window)
nb.pack(fill=tix.BOTH, expand=1)


for i in range(1,5):
	nb.add("tab"+str(i),label="Tab "+str(i))
'''
l1=tix.Label(nb.tab1,text="label "+str(1))
l1.pack()

for k in range(1,10):
    l=tix.Label(nb.tab2,text="label "+str(k))
    l.pack(side=tix.LEFT)

l3=tix.Label(nb.tab3,text="label "+str(3))
l3.pack()
'''

root.mainloop()



