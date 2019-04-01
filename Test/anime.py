from Tkinter import *
guard = 0
class Blob:

    def __init__(self, canvas, xy, ink, speed, dia, line, w):

        self.canvas = canvas

        self.id = self.canvas.create_oval(
            -50-abs(dia), -50,
            50+abs(dia), 50,
            fill=ink,
            outline=line,
            width=w
            )

        self.canvas.move(self.id, xy[0], xy[1])

        if speed > 0:
            self.delta = speed
            self.start = self.right
        else:
            self.delta = -speed
            self.start = self.left


    def __call__(self):
        return self.start # get things going

    def right(self):
        global guard
        if guard == 2:
            print self.id["outline"]
            self.id["outline"] = ""
        if guard == 0:
            xy = self.canvas.coords(self.id)
           # print xy
            if xy[2] >= self.canvas.winfo_width():
                return self.left()
            temp = self.top() 
            self.canvas.move(self.id, self.delta, temp)

        return self.right

    def left(self):
        global guard
        if guard == 2:
            print self.id["outline"]
            self.id["outline"] = ""
        if guard == 0:
            xy = self.canvas.coords(self.id)
            if xy[0] <= 0:
                return self.right()
            temp = self.down()
            self.canvas.move(self.id, -self.delta, temp)

        return self.left

    def top(self):
        if guard == 0:
            xy = self.canvas.coords(self.id)
            if xy[1] <= 0:
                return self.down()

        return -self.delta

    def down(self):
        if guard == 0:
            xy = self.canvas.coords(self.id)
            if xy[3] >=self.canvas.winfo_height():
                return self.top()
        return self.delta


def update(event):
    global guard
    if guard == 0:
        guard = 1

    elif guard == 1:
        guard = 2
    else:
        guard = 0
    


if __name__=="__main__":
    global guard
    root = Tk()
    root.title("Blobs")
    root.resizable(0, 0)

    frame = Frame(root, bd=5, relief=SUNKEN, bg="black")
    frame.pack()

    canvas = Canvas(frame, width=500, height=200, bd=0, highlightthickness=0,bg="black")
    canvas.pack()
    canvas.bind("<Button-1>", update)
    items = [
        #Blob(canvas, (100, 120), "", 0.1, 10, "white", 10),
        Blob(canvas, (100, 120), "", 0.1, 5, "white", 5),
        ]

    root.update() # fix geometry
    for i in range(len(items)):
                items[i] = items[i]()
                root.update_idletasks() # redraw
                root.update() # process events
            
    # loop over items

    try:
        while 1:
            for i in range(len(items)):
                items[i] = items[i]()
                root.update_idletasks() # redraw
            root.update() # process events
    except TclError:
        pass # to avoid errors when the window is closed
