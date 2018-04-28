
#!/usr/bin/python

class IPTree():
    def __init__(self, rootid="*"):
        self.parent = None
        self.left = None
        self.right = None
        self.rootid = rootid
        self.rules = []

    def getParent(self):
        return self.parent
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

    def insertNode(self, IP):
        # srcIP = newRule[1]
        position = self
        if not self.rootid == IP:
            # self.rules.append([newRule[0], newRule[2], newRule[3]])
        # else:
            nid = self.rootid
            if nid[-1] == "*":
                nid = nid[:-1]
            n = len(nid)
            if IP[n:n+1] == "0":
                if self.left == None:
                    if n == 31:
                        self.left = IPTree(nid+"0")
                    else:
                        self.left = IPTree(nid+"0*")
                self.left.parent = self
                position = self.left.insertNode(IP)
            else:
                if self.right == None:
                    if n == 31:
                        self.right = IPTree(nid+"1")
                    else:
                        self.right = IPTree(nid+"1*")
                self.right.parent = self
                position = self.right.insertNode(IP)

        return position


    def printTree (self):
        if self.left != None:
            self.left.printTree()
        L = self.getRuleList()
        if L != []:
            print (self.rootid, ':')
            for i  in range(len(L)):
                print (L[i].p, L[i].Action)
        if self.right != None:
            self.right.printTree()



class RuleNode():
    def __init__(self, rule):
        self.p = rule[0]
        self.Action = rule[1]
        self.srcIP = None
        self.dstIP = None





class RuleTree():
    def __init__(self):
        self.srcIP = IPTree()
        self.dstIP = IPTree()

         
    def insertRule(self, newRule):
        sIP = newRule[1]
        dIP = newRule[2]
        sNode = self.srcIP.insertNode(sIP)
        dNode = self.dstIP.insertNode(dIP)
        ruleNode = RuleNode([newRule[0], newRule[3]])
        ruleNode.srcIP = sNode
        ruleNode.dstIP = dNode
        sNode.rules.append(ruleNode)
        dNode.rules.append(ruleNode)

        # if self.rootid == srcIP:
        #     self.rules.append([newRule[0], newRule[2], newRule[3]])
        # else:
        #     nid = self.rootid
        #     if nid[-1] == "*":
        #         nid = nid[:-1]
        #     n = len(nid)
        #     if srcIP[n:n+1] == "0":
        #         if self.left == None:
        #             if n == 31:
        #                 self.left = IPTree(nid+"0")
        #             else:
        #                 self.left = IPTree(nid+"0*")
        #         self.left.parent = self
        #         self.left.insert(newRule)
        #     else:
        #         if self.right == None:
        #             if n == 31:
        #                 self.right = IPTree(nid+"1")
        #             else:
        #                 self.right = IPTree(nid+"1*")
        #         self.right.parent = self
        #         self.right.insert(newRule)

        # return None

    def getRule(self, sIP, dIP):
        return None


    def printTree (self):
        self.srcIP.printTree()
        self.dstIP.printTree()





def printTree(tree):
    if tree != None:
        printTree(tree.getLeftChild())
        print(tree.rootid, tree.getRuleList())
        printTree(tree.getRightChild())

# test  tree

def testTree():
    rules = [[1, "*", "*", 1], \
    [2, "1*", "111000101010110*", 0],
    [3, "00111*", "111000101010110*", 0],
    [4, "1001*", "111000010110*", 1],
    [5, "0011*", "1110011110110*", 0],
    [6, "0011*", "1110001110*", 0]]


    myIpTree = IPTree()    
    for i in range(len(rules)):
        myIpTree.insert(rules[i])

    printTree(myIpTree)



# testTree()
