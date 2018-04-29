#!/usr/bin/python

import csv
import SimpleFirewallDataStructure as SF
import time





# Translate IP from standard format to binary format
def ipTranslation (ip):
	[a, b, c, d] = ip.split(".")
	if not d.isnumeric() and not d == '*':
		[d, e] = d.split("/")
		e = int(e)
	else:
		e = 0
	
	ipb = ""
	if a == "*":
		ipb = ipb + "*"
	else:
		ipb = ipb + '{0:08b}'.format(int(a))
		if b == "*":
			ipb = ipb + "*"
		else:
			ipb = ipb + '{0:08b}'.format(int(b))
			if c == "*":
				ipb = ipb + "*"
			else:
				ipb = ipb + '{0:08b}'.format(int(c))
				if d == "*":
					ipb = ipb + "*"
				else:
					ipb = ipb + '{0:08b}'.format(int(d))
	
	if e:
		ipb = ipb[:-e] + "*"

	return ipb





# Read rule set from file
def readRules (filename):
	Rules = []
	p = 1
	with open(filename, newline='') as ruleFile:
		spamreader = csv.reader(ruleFile)
		for row in spamreader:
			if row[2] == 'Allow':
				A = 1
			else:
				A = 0
			Rules.append([p, ipTranslation(row[0]), ipTranslation(row[1]), A])
			p = p + 1

	return Rules



# Read traffic from file
def readTraffic (filename):
	Traffics = []
	with open(filename, newline='') as testFile:
		spamreader = csv.reader(testFile)
		for row in spamreader:
			Traffics.append([ipTranslation(row[0]), ipTranslation(row[1])])

	return Traffics





# main

# Read reuls and traffics from file
Rules = readRules ('Rules.csv')
Traffics = readTraffic ('TestIP.csv')


Tree = SF.RuleTree()
for i in range(len(Rules)):
	Tree.insertRule(Rules[i])

cacheList = list()
chacheSize = 50
# SF.printTree(sorceIP)

# Tree.printTree()

# print (Tree.srcIP.findNode('111000110001*').rootid)

max_time = 0
for i in range(len(Traffics)):
	start_time = time.time()
	if cacheList != []:
		shortList = [cacheList[j] for j in range(len(cacheList)) \
		if cacheList[j][0] == Traffics[i][0] and cacheList[j][1] == Traffics[i][1]]
		if shortList == []:
			rule = [Traffics[i][0], Traffics[i][1], Tree.getRule(Traffics[i][0], Traffics[i][1])]
			if len(cacheList) >= chacheSize:
				del cacheList[0]
			cacheList.append(rule)
		else:
			rule = shortList[0]
	else:
		rule = [Traffics[i][0], Traffics[i][1], Tree.getRule(Traffics[i][0], Traffics[i][1])]
		cacheList.append(rule)

	end_time = time.time()
	if max_time < (end_time - start_time):
		max_time = (end_time - start_time)

	if rule[2] == 2:
		print (rule)

print (max_time)
