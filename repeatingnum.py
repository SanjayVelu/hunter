defprintFirstrepeating(arr,n)
   Min = -1
   myset = dict()
   for i in range(n-1, -1, -1):
       if arr[i] in myset.keys():
           Min = i
       else:
          myset[arr[i]] = 1
   if (Min! = -1):
       print(arr[Min])
   else:
       print("unique")
arr = list(map(int,input().split()))
n = len(arr)
printFirstrepeating(arr,n)
