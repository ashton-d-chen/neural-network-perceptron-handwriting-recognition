'''
File: perceptron.py
Author: Jann-Chyi Chen
Version: 1.0
Date: 2008-03-19
Description: A perceptron classifier which can classify input image and
  train itself.
'''

from Tkinter import *
import tkFont
import temp

'''
Perceptron classifier.
'''
class PerceptronClassifier:
  def __init__( self):
    self.type = "perceptron"
    self.weights = {}

    # create a class of weights for each label
    for label in temp.LEGAL_LABELS:
      self.weights[label] = Counter()

      # initialize weights in each label class
      for i in range(28):
        for j in range(28):
          self.weights[label][(i,j)] = 0
    
  # trains the perceptron classifer by adjusting the weights of a label class
  def train( self, trainingData, trainingLabels, n, myList):

    # iterate n times for a given training data
    for iteration in range(n):
      myList.insertItem("Training iteration " + str(iteration) + ".")
      guess = []

      # iterate through different training data 
      for i in range(len(trainingData)): 
        test = 0
        vectors = Counter()

        # iterate through each legal label class, and 
        for l in temp.LEGAL_LABELS:

          # compute the score for each class of weights
          vectors[l] = self.weights[l] * trainingData[i]

          # determine whether a given legal label class has been trained
          # if so, set variable "test" to true
          if len(self.weights[l]) == 0:
            test = 0
          else:
            test = 1

        # if a class has never been train or the label having the highest
        # grade is not what the user has inputted, which mean
        # mis-recognize
        if test == 0 or vectors.argMax() != trainingLabels[i]:

          # assign the class of weights to a temp variable
          posTrainData = trainingData[i]
          negTrainData = trainingData[i]

          # for each weight value in a label class of input labe
          for j in trainingData[i]:
            if trainingData[i][j] > 0:
              # Factor each weight value in the input label class of weight
              posTrainData[j] = (temp.POS_WEIGHT)*trainingData[i][j]
              negTrainData[j] = (temp.NEG_WEIGHT)*trainingData[i][j]

          # decrease the weight value of mis-guessed class by that of
          # input datum object
          self.weights[vectors.argMax()] -= negTrainData
          
          # increase the weight value of correct class by that of
          # input datum object
          self.weights[trainingLabels[i]] += posTrainData

  # classify input datum object
  def classify(self, data, tye):
    guesses = []
    for datum in data:
      vectors = Counter()

      # find the class with greatest score
      for l in temp.LEGAL_LABELS:
        vectors[l] = self.weights[l] * datum
      guesses.append(vectors.argMax())
           
    return guesses




'''
Helper function couter
'''
class Counter(dict):

  # return the key with the highest value
  def argMax(self):
    all = self.items()
    values = [x[1] for x in all]
    maxIndex = values.index(max(values))
    return all[maxIndex][0]

  def __mul__(self, y ):

    sum = 0
    for key in self:
      if not (key in y):
        continue
      sum += self[key] * y[key]      
    return sum
      
  def __radd__(self, y):
    for key, value in y.items():
      incrementCount(key, value)   
      
  def __add__( self, y ):

    addend = Counter()
    for key in self:
      if key in y:
        addend[key] = self[key] + y[key]
      else:
        addend[key] = self[key]
    for key in y:
      if key in self:
        continue
      addend[key] = y[key]
    return addend
    
  def __sub__( self, y ):

    addend = Counter()
    for key in self:
      if key in y:
        addend[key] = self[key] - y[key]
      else:
        addend[key] = self[key]
    for key in y:
      if key in self:
        continue
      addend[key] = -1 * y[key]
    return addend
    
# inverts a matrix stored as a list of lists.
def arrayInvert(array):
  result = [[] for i in array]
  for outer in array:
    for inner in range(len(outer)):
      result[inner].append(outer[inner])
  return result


