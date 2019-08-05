def printleaders(arr,size):
    for i in range(0, size):
        for j in range(i+1, size):
            if arr[i]<=arr[j]:
               break
        if j == size-1:
            print(arr[i])
arr = input("enter a value:")
arr = list(map(int,input().split()))
printleaders(arr,len(arr))
