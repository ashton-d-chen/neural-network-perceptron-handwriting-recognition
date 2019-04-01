class Counter(dict):
  def incrementCount(self, key, count):

    if key in self:
      self[key] += count
    else:
      self[key] = count
      
  def incrementAll(self, keys, count):

    for key in keys:
      self.incrementCount(key, count)
      
  def getCount(self, key):

    if key in self:
      return self[key]
    else:
      return 0
  
  def argMax(self):
    """
    Returns the key with the highest value.
    """
    all = self.items()
    values = [x[1] for x in all]
    maxIndex = values.index(max(values))
    return all[maxIndex][0]
  
  def sortedKeys(self):
    sortedItems = self.items()
    compare = lambda x, y:  sign(y[1] - x[1])
    sortedItems.sort(compare)
    return [x[0] for x in sortedItems]
  
  def totalCount(self):
    return sum(self.values())
  
  def normalize(self):
    total = float(self.totalCount())
    for key in self.keys():
      self[key] = self[key] / total
      
  def divideAll(self, divisor):
    """
    Divides all counts by divisor
    """
    divisor = float(divisor)
    for key in self:
      self[key] /= divisor

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
    
def sign( x ):
  """
  Returns 1 or -1 depending on the sign of x
  """
  if( x >= 0 ):
    return 1
  else:
    return -1

def arrayInvert(array):
  """
  Inverts a matrix stored as a list of lists.
  """
  result = [[] for i in array]
  for outer in array:
    for inner in range(len(outer)):
      result[inner].append(outer[inner])
  return result

def pause():
  """
  Pauses the output stream awaiting user feedback.
  """
  print "<Press enter/return to continue>"
  raw_input()

def _test():
  import doctest
  doctest.testmod() 

if __name__ == "__main__":
  #_test()
  i = Counter()
  print i + 1
  
