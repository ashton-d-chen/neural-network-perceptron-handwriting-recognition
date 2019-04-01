from Tkinter import *
import time

root = Tk()
root.title("Click me!")

def next_image(event):
     # Convert the screen coordinates of the event to canvas coordinates
     x2 = canvas1.canvasx(event.x)
     y2 = canvas1.canvasy(event.y)
     x2 = int(x2)
     y2 = int(y2)

     # get the phot object coordinates
     x1, y1 = canvas1.coords('myPhoto')
     x1 = int(x1)
     y1 = int(y1)

     # create two lists of stepped x and y
     xinc = (x2 - x1)/100
     yinc = (y2 - y1)/100
     print xinc, yinc
     xlist = []
     for x in xrange(x1, x2+xinc, xinc):
         print x
         xlist.append(x)
     ylist = []
     for y in xrange(y1, y2+yinc, yinc):
         print y
         ylist.append(y)

     # move the image by the difference between the last point, sleep
     # for half a millisecond, update the display
     for i, x in enumerate(xlist):
         if i == 0:
             canvas1.move('myPhoto', x-x1, ylist[i]-y1)
         else:
             canvas1.move('myPhoto', x-xlist[i-1], ylist[i]-ylist[i-1])
         time.sleep(0.05)
         root.update()

image = "DustY1.GIF" # use any gif, this is a cartoon of my dog
photo = PhotoImage(file=image)

# make canvas the size of image1/photo1
width1 = photo.width()
height1 = photo.height()
canvas1 = Canvas(width=width1, height=height1)
canvas1.pack()

# display photo, x, y is center
x = (width1)/2.0
y = (height1)/2.0
# this is the first image
canvas1.create_image(x, y, image=photo, tags='myPhoto')  # added tags option

canvas1.bind('<Button-1>', next_image)  # bind left mouse click

root.mainloop()
