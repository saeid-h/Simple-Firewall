
#!/usr/bin/env python

class IPTree():
    def __init__(self, rootid="*"):
        self.left = None
        self.right = None
        self.rootid = rootid
        self.rules = []

    def getLeftChild(self):
        return self.left
    def getRightChild(self):
        return self.right
    def getRuleList(self):
        return self.rules

    def findNode(self, srcIP):
        if self.rootid == srcIP:
            return self
        else:
            nid = self.rootid
            if nid[-1] == "*":
                nid = nid[:-1]
            n = len(nid)
            if srcIP[n:n+1] == "0":
                return self.left
            else:
                return self.right

    def insert(self, newRule):
        srcIP = newRule[1]
        if self.rootid == srcIP:
            self.rules.append([newRule[0], newRule[2], newRule[3]])
        else:
            nid = self.rootid
            if nid[-1] == "*":
                nid = nid[:-1]
            n = len(nid)
            if srcIP[n:n+1] == "0":
                if self.left == None:
                    if n == 31:
                        self.left = IPTree(nid+"0")
                    else:
                        self.left = IPTree(nid+"0*")
                self.left.insert(newRule)
            else:
                if self.right == None:
                    if n == 31:
                        self.right = IPTree(nid+"1")
                    else:
                        self.right = IPTree(nid+"1*")
                self.right.insert(newRule)





def printTree(tree):
    if tree != None:
        printTree(tree.getLeftChild())
        print(tree.rootid, tree.getRuleList())
        printTree(tree.getRightChild())

# test  tree

def testTree():
    rules = [[1, "*", "*", 1], \
    [2, "1*", "111000101010110*", 0],
    [2, "00111*", "111000101010110*", 0],
    [2, "1001*", "111000010110*", 1],
    [2, "0011*", "1110011110110*", 0],
    [2, "0011*", "1110001110*", 0]]


    myIpTree = IPTree()    
    for i in range(len(rules)):
        myIpTree.insert(rules[i])

    printTree(myIpTree)



testTree()

