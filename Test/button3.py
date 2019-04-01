
from Tkinter import *

class Button:
    def __init__(self):
        self.root = Tk()
        self.root.title('Button Styles')
        bdw = 3
        setattr(self, 'of%d' % 3, Frame(self.root, borderwidth=0))
        Label(getattr(self, 'of%d' % 3), text='borderwidth = %d  ' % bdw).pack(side=LEFT)
        Button(getattr(self, 'of%d' % 3), text=SOLID, borderwidth=bdw, relief=SOLID, width=10,
               command=lambda s=self, r=SOLID, b=bdw: s.prt(r,b))\
                .pack(side=LEFT, padx=7-bdw, pady=7-3)
        getattr(self, 'of%d' % 3).pack()

    def prt(self, relief, border):
        
       print "hi"

myGUI = GUI()
myGUI.root.mainloop()
