m=3
n=3

a = [[2,3,4],[1,2,3]]
b = [[1,2],[2,3],[4,3]]
M = [([0] * m) for i in range(n)]
F = [([0] * m) for i in range(n)]
# print M

for i in xrange(1,m):
	M[0][i] = M[0][i-1] + b[0][i-1]
	
for j in xrange(1,n):
	M[j][0] = M[j-1][0] +a[j-1][0]

# print M
for i in xrange(1,m):
	for j in xrange(1,n):
		m1 = M[j][i-1] + b[j][i-1]
		m2 = M[j-1][i] +a[j-1][i]
		if m1 > m2:
			M[j][i] = m2
			F[j][i] = 1
		else:
			M[j][i] = m1
			F[j][i] = 2

print M
print M[m-1][n-1]

print F
def output(m,n):
	if m==0 and n == 0:
		print "(0,0)"
		return 0
	if m==0 or n ==0:
		print "(%d,%d)"%(m,n),
		print "->",
		if n == 0:
			output(m-1,n)
		else:
			output(m,n-1)
	else:
		print "(%d,%d)"%(m,n),
		print  '->',
		if F[m][n] == 2:
			output(m,n-1)
		else:
			output(m-1,n)


output(m-1,n-1)