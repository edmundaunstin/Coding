import numpy as np
x=int(input())
y=int(input())
a=list(map(str,input().split("-")))
cx,cy=int(a[0])-1,int(a[1])-1
b=list(map(str,input().split()))
mat=np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]], np.int32)
if(a[2]=='E'):
	mat[int(a[0])-1][int(a[1])-1]=3
elif(a[2]=='W'):
	mat[int(a[0])-1][int(a[1])-1]=4
elif(a[2]=='N'):
	mat[int(a[0])-1][int(a[1])-1]=1
elif(a[2]=='S'):
	mat[int(a[0])-1][int(a[1])-1]=2

for i in range(len(b)-1):
	if(mat[cx][cy]==3):
		if(b[i]=='L' and b[i+1]=='M'):
			cx=cx-1
			mat[cx][cy]=1
		elif(b[i]=='R' and b[i+1]=='M'):
			cx=cx+1
			mat[cx][cy]=2
		else:
			cy=cy+1
			mat[cx][cy]=3
	elif(mat[cx][cy]==4):
		if(b[i]=='R' and b[i+1]=='M'):
			cx=cx-1
			mat[cx][cy]=1
		elif(b[i]=='L' and b[i+1]=='M'):
			cx=cx+1
			mat[cx][cy]=2
		else:
			cy=cy-1
			mat[cx][cy]=4
	elif(mat[cx][cy]==1):
		if(b[i]=='R' and b[i+1]=='M'):
			cy=cy+1
			mat[cx][cy]=3
		elif(b[i]=='L' and b[i+1]=='M'):
			cy=cy-1
			mat[cx][cy]=4
		else:
			cx=cx-1
			mat[cx][cy]=1
	elif(mat[cx][cy]==2):
		if(b[i]=='L' and b[i+1]=='M'):
			cy=cy+1
			mat[cx][cy]=3
		elif(b[i]=='R' and b[i+1]=='M'):
			cy=cy-1
			mat[cx][cy]=4
		else:
			cy=cy-1
			mat[cx][cy]=2
			
print(mat)
if(mat[cx][cy]==1):
	s="N"
elif(mat[cx][cy]==2):
	s="S"
elif(mat[cx][cy]==3):
	s="E"
elif(mat[cx][cy]==4):
	s="W"
print(cy+1,"-",cx+1,"-",s)
