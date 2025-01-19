def brute(arr, x):
    for i in range(len(arr)):
        if arr[i] >= x:
            return i


def optimal(arr, x):
    n = len(arr)
    low, high = 0, n-1
    ans = n
    while low <= high:
        mid = (low+high)//2
        if arr[mid] >= x:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

arr = [1,2,4,12,15,19]
k = 16
print(optimal(arr, k))
