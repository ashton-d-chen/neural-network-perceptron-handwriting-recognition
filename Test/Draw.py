from WCK import Widget

class SimpleCanvas(Widget):

    ui_option_width = 100
    ui_option_height = 100

    def __init__(self, master, **options):
        self.stack = []
        self.ui_init(master, options)

    #
    # implementation

    def ui_handle_config(self):
        return int(self.ui_option_width), int(self.ui_option_height)

    def ui_handle_clear(self, draw, x0, y0, x1, y1):
        pass

    def ui_handle_repair(self, draw, x0, y0, x1, y1):
        # redraw entire stack into a pixmap
        pixmap = self.ui_pixmap(x1, y1)
        pixmap.rectangle(
            (x0, y0, x1, y1), self.ui_brush(self.ui_option_background)
            )
        for action, xy, args in self.stack:
            getattr(pixmap, action)(xy, *args)
        draw.paste(pixmap)

    #
    # canvas interface

    def append(self, action, xy, *args):
        # add item to top of stack
        index = len(self.stack)
        self.stack.append((action, xy, args))
        self.ui_damage()
        return index

    def insert(self, index, action, xy, *args):
        # insert item into stack
        self.stack.insert(index, (action, xy, args))
        self.ui_damage()
        return index

    def delete(self, index):
        # remove item from stack
        action, xy, args = self.stack.pop(index)
        self.ui_damage()
        return (action, xy) + args
		
		
from Tkinter import *

root = Tk()

w = SimpleCanvas(root)
w.pack(fill=BOTH, expand=1)

pen = w.ui_pen("black")

w.append("rectangle", [10, 10, 50, 50], w.ui_brush("red"))
w.append("rectangle", [30, 30, 70, 70], w.ui_brush("blue"))
w.append("rectangle", [50, 50, 90, 90], w.ui_brush("yellow"), pen)

def drag(event):
    # move second item to mouse coordinate
    item = list(w.delete(1))
    item[1] = event.x-20, event.y-20, event.x+20, event.y+20
    w.insert(1, *item)

w.bind("<B1-Motion>", drag)

root.mainloop()

