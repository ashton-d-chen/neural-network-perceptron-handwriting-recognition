'''
File: temp.py
Author: Jann-Chyi Chen
Version: 1.0
Date: 2008-03-19
Description: provide a place to store temporary global variable and objects
    which can be access and modified
  
'''
# label which user enters
USER_LABEL = ''
USER_ITERATIONS=5

# positive and negative learning factors
POS_WEIGHT = 1
NEG_WEIGHT = 1

# pre-defined legal labels
LEGAL_LABELS = ['0','1','2','3','4','5','6','7','8','9']

# Datum object property
DIGIT_DATUM_WIDTH=28
DIGIT_DATUM_HEIGHT=28

# previous guess label
PRE_GUESS = ''

# stores item on datum object canvas
text = []

# sotre GUI title object
iTitle = []

# store system status log object
LOG_LIST = []

# store user input canvas
inputWeight = []

# store current wieght canvas
currentWeight = []

# store system output object
iOutput = []

# store control panel object
iControl = []

# store perceptron classifier object
iClassifier = []

# store item on user input canvas
usrInputText = []

# store item on current weight canvas
curInputText = []

# mode
mode = 0
