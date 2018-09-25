row=list(map(int,input().split())) #input no. of row and column
b=[]
for i in range(0,row[0]):
    a=list(map(int,input().split()))
    b.append(a)
print(sum(b[0]))
