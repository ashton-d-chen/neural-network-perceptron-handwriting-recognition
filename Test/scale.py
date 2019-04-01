from Tkinter import *
import string
import tkFont



class theScale:
  def __init__(self, frame):


    iFrame = Frame(frame, bd=0, relief=FLAT, bg="black")
    self.iScale = Scale(iFrame, orient=HORIZONTAL,
                  length=284,
                  from_=0,
                  to=250,
                  tickinterval=50,
                  fg="#3cecff",
                  borderwidth=0,
                  bg="black",
                  relief=FLAT,
                  label="Data Amount",
                  activebackgroun="green")
    self.button = Button(iFrame, text='state', command=call).pack(side=RIGHT)
    self.iScale.grid(row=0, column=0, sticky='NE')
    self.iScale.set(100)
    self.iScale.pack(side=TOP)




  def dataAmount(self):
    print self.iScale.get()



root = Tk()
root.title('Scale')
frame = Frame(root, width=500, height=400, bd=1,bg="black")
frame.pack()
all = theScale(frame,"Data Amount")
root.mainloop()



