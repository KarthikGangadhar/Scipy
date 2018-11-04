class DoubleLinkList(object):

  def __init__(self,value):
    self.value = value
    self.nextNode = None
    self.previousNode = None


a = DoubleLinkList(1)
b = DoubleLinkList(2)
c = DoubleLinkList(3)
d = DoubleLinkList(4)

a.nextNode = b

b.previousNode = a
b.nextNode = c

c.previousNode = b
c.nextNode = d

d.previousNode = c
