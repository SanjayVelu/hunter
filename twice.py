j=int(input())
c=list(map(int,input().split()))
d=[]
for i in c:
  if(c.count(i)>1):
   d.append(i)
  else:
   print(i)
