def brute(arr, k):
    n = len(arr)

    for i in range(n):
        if arr[i] <= k:
            k += 1
        else:
            break

    return k

def optimal(arr, k):
    n = len(arr)
    low, high = 0, n-1

    while low <= high:
        mid = (low + high) // 2
        missing =  arr[mid] - (mid+1)
        if missing < k:
            low = mid + 1
        else:
            high = mid - 1

    return low + k

print(brute([1,2,3,4], 2))