def quick_sort(a):
	quick_sort2(a,0,len(a)-1)
	return a
	
def quick_sort2(a,l,h):
	  if(l<h):
	  	p=partition(a,l,h)
	  	quick_sort2(a,l,p-1)
	  	quick_sort2(a,p+1,h)
	  return a

def partition(a,l,h):
	pivotIndex=get_pivot(a,l,h)
	pivotValue=a[pivotIndex]
	a[pivotIndex],a[l]=a[l],a[pivotIndex]
	border=l
	
	for i in range(l,h+1):
		if a[i]<pivotValue:
			border+=1
			a[i],a[border]=a[border],a[i]
	a[l],a[border]=a[border],a[l]
	return border
def get_pivot(a,l,h):
	mid=(l+h)//2
	pivot=h
	if a[l]<a[mid]:
		if a[mid]<a[h]:
			pivot=mid
	elif a[l]<a[h]:
		pivot=l
	return pivot
	
a=list(map(int,input().split()))
print(quick_sort(a))
