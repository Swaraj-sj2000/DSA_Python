k=1
n=int(input())
m=[]
for i in range(n,0,-1):
    for j in range(1,i+1):
        n=[]
        n.append(k)
        k+=1
    m.append(n)

for i in range(1,n+1):
    