lis =[-1,-1]
def fin(ind,s):
	num=0.0
	while ord(s[ind])<58 and ord(s[ind])>47:
		x=ord(s[ind])-48
		num=num*10 + x
		ind+=1

	if s[ind]=='.':
		ind+=1
		div=10.000
		while ord(s[ind])<=57 and ord(s[ind])>=48:
			x=ord(s[ind])-48
			num=num+x/div
			div=div*10
			ind=ind+1


	return num

def solve(s,lis):
	n=len(s)
	for i in range(n):
		if s[i]=='(':
			lis[1]=i
		elif s[i]==')':
			lis[0]=i
			break
# lis[0]=next lis[1]=prev
s = input()
solve(s,lis)

print("Initial Circuit: " + s)
cnt=1;
while lis[1]!=-1:
	ss=""
	j=lis[1]
	k=lis[0]

	if j!=0:
		ss+=s[:j]
	print(ss)
	num=0
	a='*'
	j=j+1
	for i in range(j,k):
		if ord(s[i])<=57 and ord(s[i])>=48 and a=='*':
			store=fin(i,s)
			num=store
			i-=1
		elif ord(s[i])<=57 and ord(s[i])>=48 and a=='+':
			store=fin(i,s)
			num+=store
			i-=1
		elif ord(s[i])<=57 and ord(s[i])>=48 and a=='|':
			store=fin(i,s)
			num=(num*store)/(num+store)
			i-=1
		else:
			a=s[i]

	ss+= str(num)
	ss+=s[k+1:]
	print("Step " + str(cnt) +": " + ss)
	s=ss
	cnt+=1
	lis=[-1,-1]
	a='*'
	solve(s,lis)
