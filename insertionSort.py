def insertion_sort(a):
	for i in range(1,len(a)):
		for j in range(i-1,-1,-1):
			if(a[j]>a[j+1]):
				a[j],a[j+1]=a[j+1],a[j]
			else:
				break
	return a
a=list(map(int,input().split()))
print(insertion_sort(a))
