def min(arr,arr_size)
    inv_count = 0
    min_l = 0
    min_r = 1
    min_sum = arr[0] + arr[1]
    for l in range(0, arr_size -1):
        for r in range(l + 1, arr_size):
            sum = arr[l] + arr[r]
            if abs(min_sum) > abs(sum):
                min_sum = sum
                min_l = l
                min_r = r
    print(arr(min[l], arr(min[r])
arr = input("enter a number:")
arr = list(map(int,input().split()))
min(arr,5)

   
