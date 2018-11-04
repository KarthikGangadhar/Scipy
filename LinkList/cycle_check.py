class Node(object):

  def __init__(self,value):
    self.value = value
    self.next_node = None


def cycleCheck(node):
  marker1 = node
  marker2 = node

  while marker2 != None and marker2.next_node != None:
    marker1 = marker1.next_node
    marker2 = marker2.next_node.next_node    
    if marker1 == marker2:
      return True

    return False  

