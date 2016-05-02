def func(num):
	flag = []
	n = len(num)
	amount = [1]*n
	for i in range(n):
		k = 0
		x = 0
		for j in range(i):
			if num[i]>num[j] and k < amount[j]:# or = 
				k = amount[j]
				x = j
		amount[i] = k+1
		flag.append(x)
	for i in amount:
		print i,
	print '\n'
	print flag
# func('12349847653')

s = '2132323456789'
for i in s:
	print i,
print '\n'
func(s)