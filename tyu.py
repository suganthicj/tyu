x11=int(input())
o=[]

l=list(map(int,input().split()))
m=list(map(int,input().split()))
for i in l:
	if i in m:
		o.append(i)
z11=set(o)
z11=list(z11)
z11=sorted(z11)
print(*z11)
