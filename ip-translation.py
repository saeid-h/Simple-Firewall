#!/usr/bin/python

def ipTranslation (ip):
	[a, b, c, d] = ip.split(".")
	if not d.isnumeric():
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

