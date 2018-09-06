import operator
a=int(input())
b=int(input())
c=int(input())
dic,su,t={},0,()
for i in range(c):
	x=list(map(int,input().split()))
	pi=x[0]
	fi=x[1]
	dic[pi]=fi
	x=[]
sorted_x = sorted(dic.items(), key=operator.itemgetter(0))
sorted_x=sorted_x[::-1]
for i in range(c):
	su=su+sorted_x[i][0]
su=su+b


if(su>a):
	print("0")
else:
	d=a-su
	#print(d,su)
	for i in range(0,c):
		if(sorted_x[i][0]<d):
			su=su+sorted_x[i][0]
			#print(su)
			d=a-su
			t=t+(sorted_x[i][0],sorted_x[i][1])
			sorted_x.append(t)
	print(sorted_x)
	print(len(sorted_x))
