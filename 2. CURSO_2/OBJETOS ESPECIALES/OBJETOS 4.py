from tkinter import tix as Tix

root = Tix.Tk()
demo_maker = Tix.StringVar()
demo_maker.set('P&W')

c = Tix.Control(root, label='Engine Maker: ', variable=demo_maker, options='entry.width 10 label.width 20 label.anchor e')
c.pack(side=Tix.TOP, anchor=Tix.W)

root.mainloop()