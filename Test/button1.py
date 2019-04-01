from Tkinter import *

class App:
    def __init__(self, frame):



        self.button = Button(frame, text="QUIT", fg="red", command=frame.quit)
        self.button.pack(side=LEFT)

        self.hi_there = Button(frame, text="Hello", command=self.say_hi)
        self.hi_there.pack(side=LEFT)

    def say_hi(self):
        print "hello"
        if self.hi_there["background"] == "green":  
          self.hi_there["background"] = "yellow"
        else:
          self.hi_there["background"] = "green"

class ok:
    def __init__(self):
        root = Tk()
        frame = Frame(root)
        frame.pack()
        app = App(frame)

        root.mainloop()

ok()
