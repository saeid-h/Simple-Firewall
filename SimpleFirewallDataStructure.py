
#!/usr/bin/python

class IPTree():
    def __init__(self, rootid="*"):
        self.parent = None
        self.left = None
        self.right = None
        self.rootid = rootid
        self.rules = list()

    def getParent(self):
        return self.parent
    def getLeftChild(self):
        return self.left
    def getRightChild(self):
        return self.right
    def getRuleList(self):
        return self.rules

    def findNode(self, IP):
        if self.rootid == IP:
            return self
        else:
            i = 0
            while i < len(IP) and i < len(self.rootid) and self.rootid[i] == IP[i]:
                i = i + 1
            if i == len(IP):
                return self

            if IP[i] == '0':
                if self.left != None:
                    return self.left.findNode(IP)
                else:
                    return self
            else:
                if self.right != None:
                    return self.right.findNode(IP)
                else:
                    return self


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
            # print (self.rootid, ':')
            for i  in range(len(L)):
                print ('{0:3d} {1:32s} {2:32s} {3:1d}'.format \
                    (L[i].p, L[i].srcIP.rootid, L[i].dstIP.rootid, L[i].Action))
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

        sCurrentRules = set(sNode.rules)
        dCurrentRules = set(dNode.rules)
        intersect = sCurrentRules & dCurrentRules 
        if intersect:
            if intersect.p > newRule[0]:
                return
        
        ruleNode = RuleNode([newRule[0], newRule[3]])
        ruleNode.srcIP = sNode
        ruleNode.dstIP = dNode
        sNode.rules.append(ruleNode)
        dNode.rules.append(ruleNode)



    def getRule(self, sIP, dIP):
        currentNode = '*'
        currentRule = [0,1]
        s = 0
        ultimateNode = self.srcIP.findNode(sIP).rootid

        while currentNode != ultimateNode:

            ruleList = self.srcIP.findNode(currentNode).getRuleList()
            
            if ruleList != []:
                for i in range(len(ruleList)):
                    if isInRange(dIP, ruleList[i].dstIP.rootid):
                        if ruleList[i].p > currentRule[0]:
                             currentRule = [ruleList[i].p, ruleList[i].Action]

            if sIP[s] != '*':
                currentNode =  sIP[:s+1] + '*'
            s = s + 1

        return currentRule[1]

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


def isInRange(targetIP, rangeIP):
    if len(targetIP) < len(rangeIP):
        return False
    if len(targetIP) == len(rangeIP):
        (rangeIP == targetIP)
    if rangeIP[-1] == '*':
        for i in range(len(rangeIP)-1):
            if rangeIP[i] != targetIP[i]:
                return False
        return True                
    else:
        return (rangeIP == targetIP)

    


# testTree()
