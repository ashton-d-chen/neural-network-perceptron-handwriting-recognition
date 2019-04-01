'''
File: convert.py
Author: Jann-Chyi Chen
Version: 1.0
Date: 2008-03-19
Description: Convert a bmp image to datum object
'''

from Tkinter import *
from PIL import Image
import temp

'''
load a bmp image, crop intended part and convert it to datum object
'''
def loadImage():

  # constant for moving intended image to the center of canvas
  top = 0
  left = 27
  right = 0
  buttom = 0

  # temp variable
  result = []

  # open image
  try:
      im = Image.open("input.bmp")
      temp.LOG_LIST.insertItem("Open file...")
  except:     # if fail, throw exception
      temp.LOG_LIST.insertItem("Can't open file.")
      return
    
  # resize input image to 28 x 28 pixel
  im = im.resize((temp.DIGIT_DATUM_WIDTH,temp.DIGIT_DATUM_HEIGHT))

  # read each pixel
  for i in range(len(im.getdata())):
    result.append(im.getdata()[i])
  im = result[:]

  ### Find the top, bottom, left, and right edge of image ###
  for i in range(0,28):
    for j in range(0,28):
      if im[i*28+j] == (0,0,0):
        if top == 0:  top = i
        elif top != 0:  bottom = i
        if j < left:  left = j
        if j > right: right = j
  
  bottom = 27-bottom
  right = 27-right
  
  result = []
  first = 0
  last = 28

  ### Compare the distance of each of four edges of
  ### intended image and move image to center of canvas ###
  i = 0

  # if image is closer to top, move it down 
  if bottom-top > 1:
    for i in range((bottom-top)/2):
      result.append([])
      for j in range(0,28):
        result[i].append(' ')
    last = last-(bottom-top)/2
    i = (bottom-top)/2
    
  # if image is closer to bottom, move it up
  if top-bottom>1:
    first = (top-bottom)/2

  # read data from old image
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
    


  ### After move image to the center,
  ### convert it to a datum object and
  ### save it to a file named datum ###      
  text_file = open("datum", "w")
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

    # erase the item on canvas if there is any
    if len(temp.text) != 0:
        temp.usrInput.canvas.delete(temp.text[i])
    # print datum object on a canvas
    tempText.append(temp.usrInput.canvas.create_text(120, count, text=TEMP, fill="#3cecff", justify=CENTER, font=('courier', 10)))
    count += 10
    if i < 27:  
      text_file.write("\n")
    if i == 27:
      text_file.write(" ")
  temp.text = tempText[:]
  text_file.close()   # close the written file
  temp.LOG_LIST.insertItem("Loading completed.")
  temp.LOG_LIST.insertItem("==================")
