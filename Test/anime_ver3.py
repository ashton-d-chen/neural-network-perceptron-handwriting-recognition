import math
import Tkinter


def poly_oval(x0,y0, x1,y1, steps=20, rotation=0):
    """return an oval as coordinates suitable for create_polygon"""

    # x0,y0,x1,y1 are as create_oval

    # rotation is in degrees anti-clockwise, convert to radians
    rotation = rotation * math.pi / 180.0

    # major and minor axes
    a = (x1 - x0) / 2.0
    b = (y1 - y0) / 2.0

    # center
    xc = x0 + a
    yc = y0 + b

    point_list = []

    # create the oval as a list of points
    for i in range(steps):

        # Calculate the angle for this step
        # 360 degrees == 2 pi radians
        theta = (math.pi * 2) * (float(i) / steps)

        x1 = a * math.cos(theta)
        y1 = b * math.sin(theta)

        # rotate x, y
        x = (x1 * math.cos(rotation)) + (y1 * math.sin(rotation))
        y = (y1 * math.cos(rotation)) - (x1 * math.sin(rotation))

        point_list.append(round(x + xc))
        point_list.append(round(y + yc))

    return point_list



import Tkinter
root = Tkinter.Tk()
canvas = Tkinter.Canvas(root, width=400, height=400)

dict = {}
dict['outline'] = 'black'
dict['fill']   = 'yellow'
dict['smooth'] = 'true'

# use a polygon to draw an oval rotated 30 degrees anti-clockwise
apply(canvas.create_polygon, tuple(poly_oval(40,40, 200,300, rotation=30)),
dict)

canvas.pack()
root.mainloop()
