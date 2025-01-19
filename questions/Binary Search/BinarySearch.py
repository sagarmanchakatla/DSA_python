def BS(arr, target):
    n = len(arr)
    low, high = 0, n-1

    while low <= high:
        mid = (low+high)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid+1
        else:
            high = mid-1
    return -1

def RecurBS(arr, low, high, target):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return RecurBS(arr, low, mid-1,target)
    else:
        return RecurBS(arr, mid+1, high, target)

arr =  [1,2,3,4,5,6,7,8,9]
print(RecurBS(arr,0,len(arr)-1, 3))