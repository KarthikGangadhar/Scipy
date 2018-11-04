class SinglyLinkList(object):

  def __init__(self,value):
    self.value = value
    self.nextNode = None


a = SinglyLinkList(1)
b = SinglyLinkList(2)
c = SinglyLinkList(3)
d = SinglyLinkList(4)

a.nextNode = b
b.nextNode = c
c.nextNode = d
