# Advanced Algorithm Design
## Simple Firewall
*Saeid Hosseinpoor, Cyrus Liu, Dave*

# 1 Introduction

## 1.1 Problem Statement
  <p>The objective of this projects is design and implementation of a packet controller within a network traffic according to a set on given rules. The rules are provided in a rule file and specify whether a node and/or a sub network could pass a TCP/UDP request he other node or subnetwork. The rule format is:</p>
  <Center>srcIP(s), destIP(s), Act<Center>

  Where srcIP(s) is a single IP or a range of IPs which is sent the request, destIP(s)  is a single IP or a range of IPs which accepts the request, and Act is the action should be applied which is Allow or Block. We summary our project in two focuses showed in Fig 1.1. decision making for the coming packet a rules sets update, which means we check the different rules sets we have, find out the redundant and equivalent rules between different rules sets, then update the result to our own rules sets.
  ![alt text](https://github.com/saiedhp/Simple-Firewall/blob/master/img/project-focus.jpg "two main tasks")
                                    <center>Figure 1.1. Project Two Main Tasks</center>

  We need to design the algorithm such that be able to check the redundant rules, and for the coming package, our algorithm should check the IP and return the action for the IP pairs according our rules file. Some rules may apply to a pair of source and destination IPs, if they imply the same action, it is safe to pick one of them. The problem rises when we have different action for a single pair of IPs. For this situation, we look at the assigned priority to each rule and pick the most important rule.


# 1.2 Assumptions

  IPs are defined in standard formats of a.b.c.d which a-d are integer numbers between 0 and 255. Range of IPs described in standard form of a.b.c.* or a.b.c.d/e or similar standard forms. There is no guaranty of consistency in rules or avoiding redundancies. Since, we assume rules are added to the list with no consideration, we make another assumption that most recent rules have higher priority to apply. For sake of clarity, we assume that new rules added to the end of the available rule file. The rules on the top of the file, are older than rules in the bottom of the file.

  A private repository on github was created for group members to ease up working on the project simultaneously. Python 3 was adopted as an implantation language.

# 2 Design

  First of all, we need a data structure that is capable to fast store and access of IP addresses and range of the IP addresses. In order to define such data structure, we need to define an unique and useful form of IP addresses and ranges that could be easier to store or recover. Fig 2.1 shows the format of rules sets that we implement in out project, there are four parts, the first one is the  priority which we use to make the decisions for multiple match result of coming packet, we pick the highest priority one. Then followed by the source IP and destination IP, then the action which is whether allow or block in our cases.
  ![alt text](https://github.com/saiedhp/Simple-Firewall/blob/master/img/rules-node.png "rule node")
  Figure 2.1. IP Rule Set Format

## 2.1 IP Translation
i
  We know that an IP address is in form of d.d.d.d which d is an integer number between 0 and 255. Therefore we can translate each integer number into a 8-bit binary number. According to this mapping function we have a string of 32 bit of 0s and 1s.

   <Center>IP → “d1 …  d32“   di ∈ {0,1}<Center>

   For the range of IPs, we can use * as a wild char define whatever after fixed bits:

<Center>IP-Range → “d1 …  dk*”   di ∈ {0,1}<Center>

## 2.2 Data Structure
i
  Inspiring by the hierarchy concept of IP addresses we define a binary search tree to store the IP address and ranges. The translation of the IP address and range into an IPString, helps us to define this  binary tree, such that the left child of a node is the next 0 after current node, and the right child is the next 1 after current node.

  We store our source IP and destination IP into two different binary trees, then connect them with rules table showed in Fig 2.2, when the coming packet checked by our rules sets,  we search the IP we get the rules result at the same time, then we check the destination IP tree, we also get the action result, then we choose the higher priority one applying the rule to this packet.
    ![alt text](https://github.com/saiedhp/Simple-Firewall/blob/master/img/rule-tree.png "rule tree")
    Figure 2.2. Rules Sets Data Structure

  Let’s consider the root of the tree be “*” which is range of all IPs (*.*.*.*), the left child of root represent “0*” and the right child is “1*” and so on. In other words if we have a node of  “d1 …  dk*”, the left child of this node is “d1 …  dk0*”, and the right child is “1d1 …  dk1*”. Fig.2.3. shows how we construct the IP tree. It is obvious that the parent of this node would be “d1 …  dk-1*”. As a result of this definition, leaves are single IP address and intermediates nodes are IP ranges.
  ![alt text](https://github.com/saiedhp/Simple-Firewall/blob/master/img/IPTree.jpg "IP tree")
         Figure 2.3. Basic Binary Tree for IP Storage

  The maximum height of this tree is 32 which is the maximum length of the IPString. Access to the nodes in the worst case is 32 operation which is O(1), in Fig 2.4. we show an example of a specific rule stored in our data structure.
  ![alt text](https://github.com/saiedhp/Simple-Firewall/blob/master/img/rules_tree_example.png "rules tree instance")
  Figure 2.4. Source IP and Destination IP Rules Linking
i
# 3 Implementation

  We need to implement different operations like insertion, search, match, and update in this project. More operations might be added if they are required during the development phase. For the coming packet checking part, as we showed in Fig 3.1. we first search the source IP and destination IP in the cahe rule list, if we don’t get the result, we get back to our whole rule sets stree, then we search the rules tree, apply the results to the coming packet.
  ![alt text](https://github.com/saiedhp/Simple-Firewall/blob/master/img/search.png "search")
  Figure 3.1. Info Query from Tree Structure

## 3.1 Insertion

  After IP translation we start from root and traverse the tree to find the source IP(s)’s position in the tree. If the children are available we go through the nodes until get the target node, then insert the rule into a table or link list of the rules. In such case that children are not available we make new child in proper position and open a new list or table of rules in the final node.
We investigated to consider two tree for source and destination IPs, but analysis shows that it doesn’t improve the performance.

## 3.2 Search

  IPString, translated IP address or range, is a unique representation of various form of IP address or ranges. We find the source IP as described in the insertion operation, then retrieve the rule table. We pick all the rules from the nodes in the path from root to source IP node which matches the destination IP because all the parent rules should be applied to the traffic packet. The most important rule, based on priority, will be applied to the traffic packet.

## 3.3 Update

  Similar to insertion operation, we will find the position of the rule. The difference is that we add the rule to the node if its priority is higher than the redundant rule or there is no redundant rule in the rule list ignore it. This strategy might be updated and improved in future. As for the redundant  and equivalent checking of different rules sets, we have a coming new rule, as it showed in Fig 3.2. we first search it in our rules sets tree,and get the rules node information and check the results, if we have the same source IP and destination IP, then comes the same action result, otherwise with different actions we report a conflict. In another situation, we the new rule IP is in the range of our rules sets, we report that they are redundant.
  ![alt text](https://github.com/saiedhp/Simple-Firewall/blob/master/img/update.png "update")
  Figure 3.2. Update the Rules Set to Our Data Structure

## 3.4 Match

  This is boolean function that check whether an IP address (e.g. destination address) in equal to the given IP address or is in the range of a given IP range. In other words, it checks if a given IPString covers or equals to other IPString.

# 4 Analysis
## 4.1 Time Complexity

  The time complexity of creation of the data list is O(n), because we need to add, insert each n rules in the data structure in constant time. However the complexity for search and reaching the node related to the source IP is O(1). In the worst case that all the rules are related to the source IP, we need two comparison for destination IP and rule’s priority to verify the relevance of the rules. The maximum number is O(n).

  For a request that took place most recently, we just have constant time O(1) operation to find it within the most recent list and apply it again.

## 4.2 Space Complexity

  In the worst case, we need O(log n) nodes to store data where n is the total number of the rules (proof is available). Each rule needs a unit space to store, in worst case that rules are unique and there is no redundancy or conflict in rule set. Therefore the total space required is O(n+log n) which is O(n).

# 5 Optimization

  Since the traffic between specific IPs happens frequently, we make a limited size of the most recent rules applied to the network traffic, this list is separated from our binary tree . We first check the list when a traffic request comes, if the rules are not on the recent list, we search back to our whole rule sets. This list will be updated after each event. The event is applying a rule to traffic or any changes in rule sets. In reality, as the coming traffic streams constantly, the recent rule list makes the firewall faster because we know that every nodes in Internet does not request to connect to other nodes by checking our whole rules table. Access to this list is very fast, which is in constant time O(1). Fig 5.1 shows a another type of tree structure which has a better time complexity for the rules conflicts detection, we will investigate more about this kD-tree structure, and apply to our approach to improve our performance.
  ![alt text](https://github.com/saiedhp/Simple-Firewall/blob/master/img/optimization.png "optimization")
  Figure 5.1. A Rectangle Rule Conflicts Checking

# References
