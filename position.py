def Rearrange(arr,n):
    j = -1
    for i in range(0,n):
        if (arr[i] % 2 == 0):
            j = j+1
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
arr=input("enter the number:")
arr = list(map(int,input().split()))
n = len(arr)
rearrange(arr,n)
for i in range(0,n):
    print(arr[i], end= "")
