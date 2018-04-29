




A = [1,2, 3, 4, 5]

print (A)
print (A[1])

B = []

print (B)
if B == []:
	print (B)


A = 'dsffs'
B = 'ASDAF'

print (A[2]+B[3])

A = [[1,2,3], [1,2,4], [2,1,1]]
B = [A[i] for i in range(3) if A[i][0] == 1]
print (B)
print (A)
del A[0]
print (A)