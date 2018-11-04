class Node(object):

  def __init__(self,value):
    self.value = value
    self.next_node = None

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.next_node = b
b.next_node = c
c.next_node = d
d.next_node = e

def reverseLinkList(head):
  currentNode = head
  previousNode = None
  nextNode = None

  while currentNode:

    nextNode = currentNode.next_node
    currentNode.next_node = previousNode

    previousNode = currentNode
    currentNode = nextNode

  return previousNode

reversed_link_list = reverseLinkList(a) 
print(reversed_link_list.value)
x = reversed_link_list.next_node
print(x.value)
y = x.next_node
print(y.value)
z = y.next_node
print(z.value)



  