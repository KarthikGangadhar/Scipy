class stack(object):

  def __init__(self):
    self.items = []

  def isEmpty(self):
    return self.items == []

  def push(self, item):
    self.items.append(item)

  def pop(self):
    if self.items != []:
      return self.items.pop()

  def size(self):
    return len(self.items)

class queue(object):
  
  def __init__(self):
    self.s1 = stack()
    self.s2 = stack()

  # def isEmpty(self):
  #   return self.s1.isEmpty() and self.s2.isEmpty()

  # def size(self):
  #   return self.s1.size() + self.s2.size()

  def enqueue(self, item):
    self.s1.push(item)

  def dequeue(self):
    if not self.s2:
      while self.s1:
        self.s2.push(self.s1.pop())
      return self.s2.pop()