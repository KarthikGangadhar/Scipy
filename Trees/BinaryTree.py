class BinaryTree(object):

  def __init__(self,key):
    self.key = key
    self.leftChild = None
    self.rightChild = None

  def insertLeftChild(self, value):
    if self.leftChild == None:
      self.leftChild = BinaryTree(value)
    else:
      t = BinaryTree(value)
      t.leftChild = self.leftChild
      self.leftChild = t

  def insertRightChild(self,value):
     if self.rightChild == None:
       self.rightChild = BinaryTree(value)
     else:
       t = BinaryTree(value)
       t.rightChild = self.rightChild
       self.rightChild = t

  def getLeftChild(self):
    return self.leftChild

  def getRightChild(self):
    return self.rightChild

  def getRootVal(self):
    return self.key

  def setRootVal(self,value):
    self.key = value       


tree = BinaryTree("a")
print(tree.getRootVal())
print("leftchild before :",tree.getLeftChild())
tree.insertLeftChild("b")
tree.insertLeftChild("d")
print("leftchild after :",tree.getLeftChild().getRootVal())
print("rightchild before :",tree.getRightChild())
tree.insertRightChild("c")
tree.insertRightChild("e")
print("rightchild after :",tree.getRightChild().getRootVal())