aa=int(input())
n=list(map(int,input().split()))
li=[]
for x in range (aa):
    for i in range(x+1,len(n)):
        if(n[i]==n[x]):
          li.append(n[x])
if(len(li)==0:
   print("unique")
else:
    li.sort()
    li2=set(li)
    for x in li2:
        print(x,end=' ')
  
    
