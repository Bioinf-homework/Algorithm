
a = [1,5,2,3]
o = ['/','-','*']

n = len(a)

# A = [[0]*n]*n

A = [([0] * n) for i in range(n)]
B = [([0] * n) for i in range(n)]
# print A

for i in range(n):
	# a[][] = str1
	A[i][i] = a[i]
	# print a[i]

# print A


for l in range(1,n):
	for i in range(0,n-l):
		j = i + l
		max_num = 0
		flag = 0
		for k in range(i,j):
			print k,
			if o[k] == '+':
				num = A[i][k] + A[k+1][j]
			if o[k] == '-':
				num = A[i][k] - A[k+1][j]
			if o[k] == '*':
				num = A[i][k] * A[k+1][j]
			if o[k] == '/':
				num = (1.0*A[i][k])/(1.0*A[k+1][j])

			if num > max_num:
				max_num = num
				flag = k

    
		A[i][j] = max_num
		B[i][j] = flag
		print '\n'

print A

print A[0][n-1]
# k = B[0][n-1]
# while 1:
	
# 	pass

