
import sys
from Tkinter import *
import tkFont

STATUS_X = 80
STATUS_Y = 40
c1 = 0
c2 = 0
c3 = 0
c4 = 0
c5 = 0
myList = 0


def loadImage():
  from PIL import Image
  WIDTH = 28
  HEIGHT = 28
  temp = Image.open("digitdata/input.bmp")
  im = temp.resize((WIDTH,HEIGHT))
  im = list(im.getdata())
  result = []

  for i in range(0,28):
    test = ''
    for j in range(0,28):
      if im[i*28+j] == (255,255,255):
        result.append(' ')
      elif im[i*28+j] == (0,0,0):
        result.append('#')
      test += result[i*28+j]
    print test

  text_file = open("digitdata/testingimages", "w")
  for i in range(0,27):
    test = ''
    for j in range(0,27):
      if result[i*28+j] == ' ':
        if result[(i+1)*28+j] == '#':
          result[i*28+j] = '+'
        elif result[(i-1)*28+j] == '#':
          result[i*28+j] = '+'
        elif result[i*28+j+1]== '#':
          result[i*28+j] = '+'
        elif result[i*28+j-1] == '#':
          result[i*28+j] = '+'
          
      text_file.write(result[i*28+j])
    text_file.write(" ")
    text_file.write("\n")
  text_file.write("                            ")
  text_file.write("\n")
  text_file.write("                            ")
  text_file.close()




class theList:
    def __init__(self,root):
        frame = Frame(root, height=15, width=18, bg="black")
        

        self.l = Listbox(frame, height=15, width=18,bg = "black", fg="green", font=('times', 12))
        scroll = Scrollbar(frame, command=self.l.yview)

        self.l.configure(yscrollcommand=scroll.set)
        self.l.pack(side=LEFT)
        scroll.pack(side=LEFT, fill=Y)
        #frame.pack(expand=1, fill=X,pady=10,padx=5,sid="top")
        frame.pack(side="left")

    def insertItem(self,message):
        self.l.insert(END, message)
        self.l.see(END)


class myButton:
    def __init__(self, frame):

        self.start = Button(frame, text="Load User Input", fg="#3cecff", command=self.loadImage, bg ="black", relief=SOLID)
        self.start.pack(side=RIGHT)
        
        self.button = Button(frame, text="QUIT", fg="#3cecff", command=frame.quit(), bg="black", relief=SOLID)
        self.button.pack(side=RIGHT)
        
    def loadImage(self):
        global c2, STATUS_Y, myList

        if self.start["background"] == "Blue":  
          self.start["background"] = "Black"
        else:
          self.start["background"] = "blue"
          self.start["fg"] = "#FFF"
          myList.insertItem("Loading User Image...")
          loadImage()
          
    def goQuit(self):
        root.exit()
          
class AllTkinterWidgets:
    def __init__(self, master):
        global c1, c2, c3, c4, c5, myList
        frame = Frame(master, width=700, height=600, bd=1, background ="black")
        frame.pack()
       
        iframe5 = Frame(frame, bd=0, relief=FLAT, background ="black")
        iframe5.pack(expand=1, fill=X, pady=10, padx=5,side="top")
        c1 = Canvas(iframe5, bg='white', width=700, height=50,background="black")
        c1.pack()

     
        iframe5 = Frame(frame, bd=0, relief=RAISED, background ="black", highlightcolor="red")
        iframe5.pack(expand=1, fill=X, pady=10, padx=5,side="bottom")
        c6 = Canvas(iframe5, width=700, height=50,background="black")
        c6.pack()

        # Status Frame
        iframe5 = Frame(frame, bd=0, relief=RAISED,  background ="black")
        iframe5.pack(expand=1, fill=X, pady=10, padx=5, side="left")
        lbl = Label(iframe5, text = "System Status", fg="#3cecff", bg="black",font=("times",14,"bold"))
        lbl.pack()
     #   c2 = Canvas(iframe5, bg='white', width=175, height=400,background="black")
        #c2.pack()

        # Add a log list
        myList = theList(iframe5)
        for i in range(40):
            myList.insertItem(i)

        # User Input Frame 
        iframe5 = Frame(frame, bd=0, relief=RAISED,  background ="black")
        iframe5.pack(expand=1, fill=X, pady=10, padx=5, side="left")
        c3 = Canvas(iframe5, width=175, height=400,background="black")
        c3.pack()       
     #   lb2 = Label(iframe5, text = "User Input", fg = "Blue", bg = "black", font = ("courier",12))
   #     lb2.pack()
        
        
        # System Output Frame
        iframe5 = Frame(frame, bd=0, relief=RAISED,  background ="black")
        myButton(iframe5)
        iframe5.pack(expand=1, fill=X, pady=10, padx=5, side="right")
        c5 = Canvas(iframe5, bg='white', width=175, height=400, background="black")
        c5.pack()


        c1.create_text(330, 25, text='Perceptron Handwriting Recognition', fill="#3cecff", justify=CENTER,font=('Times', 20, 'bold'))
        c3.create_text(80, 20, text='User Input', fill="#3cecff", justify=CENTER, font=('times', 14, 'bold'))
        c3.create_text(80, 280, text='Predicted', fill="#3cecff", justify=CENTER, font=('times', 14, 'bold'))
        c3.create_text(80, 296, text='Correctness', fill="#3cecff", justify=CENTER, font=('times', 14, 'bold'))
        


        c5.create_text(80, 20, text='Guess Digit', fill="#3cecff", justify=CENTER, font=('times', 14, 'bold'))
        c5.create_text(80, 280, text='Correctness', fill="#3cecff", justify=CENTER, font=('times', 14, 'bold'))
        c5.create_text(80, 296, text='Statistics', fill="#3cecff", justify=CENTER, font=('times', 14, 'bold'))
        c6.create_text(80, 20, text='Statistics', fill="#3cecff", justify=CENTER, font=('times', 14, 'bold'))





       # for i in range(30): 
         #  L.insert(Tkinter.END, str(i)*3)


        # Initialize buttons
        
        
    
root = Tk()
root.option_add('*font', ('verdana', 10, 'bold'))
all = AllTkinterWidgets(root)
root.title('Tkinter Widgets')
root.mainloop()
