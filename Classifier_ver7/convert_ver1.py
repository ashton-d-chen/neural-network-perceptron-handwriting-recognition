from Tkinter import *
from PIL import Image
import temp
import log

def loadImage():
  
  WIDTH = 28
  HEIGHT = 28
  top = 0
  left = 27
  right = 0
  buttom = 0
  try:
      TEMP = Image.open("digitdata/input.bmp")
      temp.LOG_LIST.insertItem("Open file...")
  except:
      temp.LOG_LIST.insertItem("Can't open file.")
      return
  im = TEMP.resize((WIDTH,HEIGHT))
  TEMP = []
  for i in range(len(im.getdata())):
    TEMP.append(im.getdata()[i])
  im = TEMP[:]
  result = []

  for i in range(0,28):
    test = ''
    result.append([])
    for j in range(0,28):
      if im[i*28+j] == (255,255,255):
        result[i].append(' ')
      elif im[i*28+j] == (0,0,0):
        result[i].append('#')
        if top == 0:
          top = i
        if top != 0:
          bottom = i
        if j < left:
          left = j
        if j > right:
          right = j
      test += result[i][j]
  rrr = result

  bottom = 27 - bottom
  right = 27 - right
  
  result = []
  first = 0
  last = 28

  i = 0
  if bottom-top>1:
    for i in range((bottom-top)/2):
      result.append([])
      for j in range(0,28):
        result[i].append(' ')
    last = last-(bottom-top)/2
    i = (bottom-top)/2
  if top-bottom>1:
    first = (top-bottom)/2
  
  for g in range(first,last):
    test = ''
    start = 0
    end = 28
    result.append([])
    if (left-right) > 1:
      start = (left-right)/2
    if (right-left) > 1:
      end = end - (right- left)/2
      for h in range((right-left)/2):
        result[i].append(' ')
   
    for j in range(start,end):
      if im[g*28+j] == (255,255,255):
        result[i].append(' ')
      elif im[g*28+j] == (0,0,0):
        result[i].append('#')
    if (left-right) > 1:
      for t in range((left-right)/2):
        result[i].append(' ')
    i += 1
  if top-bottom>1:
    for g in range((top-bottom)/2):
      result.append([])
      for j in range(0,28):
        result[i].append(' ')
      i += 1
    


      
  text_file = open("digitdata/testingimages", "w")
  count = 20
  tempText = []
  for i in range(0,28):
    TEMP = ''
    for j in range(0,28):
      if result[i][j] == ' ':
        if i < 27 and result[i+1][j] == '#':
          result[i][j] = '+'
        elif i > 0 and result[i-1][j] == '#':
          result[i][j] = '+'
        elif j < 27 and result[i][j+1]== '#':
          result[i][j] = '+'
        elif j > 0 and result[i][j-1] == '#':
          result[i][j] = '+'
      TEMP += result[i][j]
      text_file.write(result[i][j])
    if len(temp.text) != 0:
        temp.c3.delete(temp.text[i])
    tempText.append(temp.c3.create_text(120, count, text=TEMP, fill="#3cecff", justify=CENTER, font=('courier', 10)))
    count += 10
    if i < 27:
      text_file.write("\n")
    if i == 27:
      text_file.write(" ")
  temp.text = tempText[:]
  text_file.close()
  temp.LOG_LIST.insertItem("Loading completed.")
  temp.LOG_LIST.insertItem("==================")

# Test Module
if __name__=="__main__":
  root = Tk()
  frame = Frame(root)
  frame.pack()
  temp.c3 = Canvas(frame)
  temp.LOG_LIST = log.theLog(frame)
  loadImage()
