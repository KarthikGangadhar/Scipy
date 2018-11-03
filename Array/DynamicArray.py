import ctypes

class DynamicArray(object):

  def __init__(self):
    # need 3 fields
    # 1. n -To hold the array length
    # 2. capacity to hold the current Array size 
    # 3. A - The array to contain data
    self.n = 0
    self.capacity = 1
    self.A = self.make_array(self.capacity)

  def __len__(self):
    # returns the current array size
    return self.n

  def __getitem__(self,k):
    # check the index for overflow, And throw error
    if not 0 <= k <= self.n:
      return IndexError("Index is out of bound")

    # return requested element
    return self.A[k]  

  def make_array(self,new_size):
    # create a new array with the request size
    return (new_size * ctypes.py_object)()

  def append(self, ele):
    # check for overflow, and create a new array if size exceeds
    if self.n == self.capacity:
      self._resize(2 * self.capacity) 

    self.A[self.n] = ele
    self.n += 1

  def _resize(self, size):
    # create a new array with double size
    B = self.make_array(size)

    # assign all the elements to new array
    for k in range(self.n):
      B[k] = self.A[k]

    # assign new array  to original array
    self.A = B
    self.capacity = size
    print("updated capacity: {0}".format(self.capacity))

arr = DynamicArray()

for i in range(1000):
  arr.append(i)

