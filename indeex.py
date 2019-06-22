a=int(input())
b=list(map(int,input().split()))
c=[]
for i in b:
    if(i==b.index(i)):
        c.append(i)
print(*(sorted(c)))
if(len(c)==0:
    print(-1)
