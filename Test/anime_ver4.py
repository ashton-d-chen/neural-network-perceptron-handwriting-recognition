from Tkinter import *

import math
import cmath

c = Canvas(width=200, height=200)
c.pack()
CENTER_X = 100
CENTER_Y = 100
NUM = 4
RADIUS1 = 50*math.sqrt(2)
RADIUS2 = RADIUS1 - 20
xy1 = []
xy2 = []
print math.exp(NUM)
for i in range(NUM):
	xy1.append((CENTER_X+(RADIUS1*cmath.exp(i*2*math.pi/NUM*1j)).real,CENTER_Y+(RADIUS1*cmath.exp(i*2*math.pi/NUM*1j)).imag))

for i in range(NUM):
	xy2.append((CENTER_X+(RADIUS2*cmath.exp(i*2*math.pi/NUM*1j))\
                    .real,CENTER_Y+(RADIUS2*cmath.exp(i*2*math.pi/NUM*1j)).imag))

polygon_item1 = c.create_polygon(xy1,fill="#3cecff")
polygon_item2 = c.create_polygon(xy2,fill="white")
center = 100, 100

frame = Frame(root, width=50, height=100)
def getangle(event):
    dx = c.canvasx(event.x) - center[0]
    dy = c.canvasy(event.y) - center[1]
    try:
        return complex(dx, dy) / abs(complex(dx, dy))
    except ZeroDivisionError:
        return 0.0 # cannot determine angle

def press(event):
    # calculate angle at start point
    global start
    start = getangle(event)

def motion(event):
    # calculate current angle relative to initial angle
    global start
    angle = getangle(event) / start
    offset = complex(center[0], center[1])
    newxy1 = []
    for x, y in xy1:
        v = angle * (complex(x, y) - offset) + offset
        newxy1.append(v.real)
        newxy1.append(v.imag)
    c.coords(polygon_item1, *newxy1)

c.bind("<Button-1>", press)
c.bind("<B1-Motion>", motion)

mainloop()
