def brute(arr, target):
    first, last = -1, -1
    n = len(arr)
    for i in range(n):
        if arr[i] == target:
            if first == -1:
                first = i
            else:
                last = i
    return [first, last]


def binarysearch(arr, target):
    first = -1
    last = -1
    n = len(arr)
    low, high = 0, n-1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            first = mid
            high = mid - 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    low, high = 0, n-1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            last = mid
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    print(first, last)


binarysearch([5,7,7,8,8,10], 8)
