# simple binary treei
# in this implementation, a node is inserted between an existing node and the root
#!/usr/bin/env python

class BinaryTree():
    def __init__(self,rootid):
        self.left = None
        self.right = None
        self.rootid = rootid
        def getLeftChild(self):
            return self.left
        def getRightChild(self):
            return self.right
        def setNodeValue(self,value):
            self.rootid = value
        def getNodeValue(self):
            return self.rootid


        def insertRight(self,newNode):
            if self.right == None:
                self.right = BinaryTree(newNode)
            else:
                tree = BinaryTree(newNode)
                tree.right = self.right
                self.right = tree

        def insertLeft(self,newNode):
            if self.left == None:
                self.left = BinaryTree(newNode)
            else:
                tree = BinaryTree(newNode)
                self.left = tree
                tree.left = self.left


def printTree(tree):
    if tree != None:
        printTree(tree.getLeftChild())
        print(tree.getNodeValue())
        printTree(tree.getRightChild())

# test  tree

def testTree():
    myIpTree = BinaryTree("Root")
    myIpTree.insertLeft("0")
    myIpTree.insertRight("1")
    myIpTree.insertRight("1")
    printTree(myIpTree)
