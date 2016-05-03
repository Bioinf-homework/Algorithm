S = [1,2,3,4,5,6,7]

n = len(S)

t = sum(S)/2

M = [([0] * (t+1)) for i in range(n+1)]
F = [([1] * (t+1)) for i in range(n+1)]

for j in range(1,t+1):
	for i in range(1,n+1):
		if j - S[i-1] >= 0:
			m1 = M[i-1][j-S[i-1]]+S[i-1]
			m2 = M[i-1][j]
			if m2 >= m1:
				M[i][j] = m2
				F[i][j] = 2
			else:
				M[i][j] = m1
			# M[i][j] = max(m1,m2)
		else:
			M[i][j] = M[i-1][j]

print M
print F