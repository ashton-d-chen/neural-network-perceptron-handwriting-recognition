from Tkinter import *

class Blob:

    def __init__(self, canvas, xy, ink, delta):

        self.canvas = canvas

        self.id = self.canvas.create_rectangle(
            -10-abs(delta), -10,
            11+abs(delta), 11,
            fill=ink
            )

        self.canvas.move(self.id, xy[0], xy[1])

        self.delta = delta
        self.start = self.right

    def __call__(self):
        return self.start # get things going

    def right(self):
        global X, Y
        xy = self.canvas.coords(self.id)
        if xy[2] < self.canvas.winfo_width():        
            self.canvas.move(self.id, self.delta, 0)

        return self.right



def callback(event):
    global X, Y
    X = event.x
    Y = event.y
    canvas = Canvas(frame, width=500, height=200, bd=0, highlightthickness=0)
    canvas.pack()
    canvas.create_rectangle(X,Y,X+10,Y+10)
    
    print "clicked at", event.x, event.y

X = 0
Y = 0
root = Tk()
root.title("Blobs")
root.resizable(0, 0)

frame = Frame(root, width= 500, height=200, bd=5, relief=SUNKEN)
frame.bind("<Button-1>", callback)
frame.pack()
print 'cp1'
root.mainloop()
print 'cp2'

canvas = Canvas(frame, width=500, height=200, bd=0, highlightthickness=0)

canvas.pack()

items = [
    Blob(canvas, (100, 50), "red", 5),
    ]

root.update() # fix geometry

# loop over items

try:
    while 1:
        for i in range(len(items)):
            items[i] = items[i]()
            root.update_idletasks() # redraw
        root.update() # process events
except TclError:
    pass # to avoid errors when the window is closed
