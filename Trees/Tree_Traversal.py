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

tree = BinaryTree(21)

for i in range(20):
  if i % 2 == 1:
    tree.insertLeftChild(i)
  else:
    tree.insertRightChild(i)

def preOrder(tree):
    if tree != None:
      print("preOrder() :",tree.getRootVal())
      preOrder(tree.getLeftChild())
      preOrder(tree.getRightChild())

def inOrder(tree):
    if tree != None:
      inOrder(tree.getLeftChild())
      print("inOrder() :",tree.getRootVal())
      inOrder(tree.getRightChild())
      
def postOrder(tree):
    if tree != None:
      postOrder(tree.getLeftChild())
      postOrder(tree.getRightChild())
      print("postOrder() :",tree.getRootVal())


preOrder(tree)
postOrder(tree)
inOrder(tree)