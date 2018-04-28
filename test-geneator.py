
#!/usr/bin/env python


import csv
import random

random.seed(1000)

def generateTrafficIP ():
	a = str(random.randint(1,255))
	b = str(random.randint(0,255))
	c = str(random.randint(0,255))
	d = str(random.randint(0,255))
	ip = str(a) + '.' + str(b) + '.' + str(c) + '.' + str(d)
		
	return ip



trafficFile = open('TestIP.csv', 'w')

Traffics = []
t = [generateIP(), generateIP()]
Traffics.append(t)
for i in range(1000):
	p = random.randint(1,10)
	if p < 4:
		i = random.randint(0,len(Traffic)-1)
		t = Traffic[i]
	elif p < 9:
		t = Traffic[-1]
	else:
		t = [generateIP(), generateIP()]
	Traffics.append(t)

print (Traffics)


with trafficFile:
    writer = csv.writer(trafficFile)
    writer.writerows(Traffics)

print("Writing complete")

