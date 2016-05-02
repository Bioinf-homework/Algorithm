def func(num,d):
	flag = []
	n = len(num)
	amount = [1]*n
	for i in range(n):
		k = 0
		x = 0
		for j in range(i):
			if abs(int(num[i])-int(num[j])) <= d and k <= amount[j]:# or = 
				k = amount[j]
				x = j
		amount[i] = k+1
		flag.append(x)
	for i in amount:
		print i,
	print '\n'
	print flag
	return flag,amount
def output(num,amount,flag):

	maxnum = amount[0]
	for i in range(len(amount)):
		if amount[i] > maxnum:
			maxnum = amount[i]
			k = i
	print 'sequence lenth:'+str(maxnum)

	while 1:
		print num[k]
		k = flag[k]
		if amount[k] == 1:
			print num[k]
			break

# func('12349847653')
s = [12,11,10,13,15,13,14,11]
# s = '2132323456789'
for i in s:
	print i,
print '\n'
flag,amount = func(s,2)
output(s,amount,flag)