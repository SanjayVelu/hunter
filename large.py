a=int(input())
l=[int(x) for x in input().split()]
l.sort()
for i in range(k-1,-1,-1):
  print(l[i],end=' ')
