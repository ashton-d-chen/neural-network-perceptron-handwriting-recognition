'''
File: Samples.py
Author: Jann-Chyi Chen
Version: 1.0
Date: 2008-03-19
Description: Read a datum object and return the vectors of datum object
  
'''
import util
from Tkinter import *
import tkFont
import temp
## Constants
DATUM_WIDTH = 0 # in pixels
DATUM_HEIGHT = 0 # in pixels

'''
Creates a datum object from the file input
'''
class Datum:
  def __init__(self, data,width,height):
    DATUM_HEIGHT = height
    DATUM_WIDTH=width
    self.height = DATUM_HEIGHT
    self.width = DATUM_WIDTH
    if data == None:
      data = [[' ' for i in range(DATUM_WIDTH)] for j in range(DATUM_HEIGHT)] 
    self.pixels = util.arrayInvert(convertToInteger(data))

  
  # Return the value of pixel at specified location
  def getPixel(self, column, row):
    return self.pixels[column][row]

  # return all the pixel
  def getPixels(self):
    return self.pixels    

# read datum file and return a datum object
def loadDataFile(filename,n,width,height,myList):
  DATUM_WIDTH=width
  DATUM_HEIGHT=height
  fin = open(filename)
  items = []
  ok = []

  for i in range(n):
    data = []
    for j in range(height):
      temp = fin.readline()
      data.append(list(temp)[:-1])
    items.append(Datum(data,DATUM_WIDTH,DATUM_HEIGHT))
  fin.close()

  testData = map(getVector, items)
  return testData

# convert pixels in datum object to integer
def convertToInteger(data):
  if type(data) != type([]):
    if(data == ' '):
      return 0
    elif(data == '+'):
      return 1
    elif(data == '#'):
      return 2           
  else:
    return map(convertToInteger, data)


def getVector(datum):
  a = datum.getPixels()

  features = util.Counter()
  for x in range(temp.DIGIT_DATUM_WIDTH):
    for y in range(temp.DIGIT_DATUM_HEIGHT):
      if datum.getPixel(x, y) > 0:
        features[(x,y)] = 1
      else:
        features[(x,y)] = 0
  return features
