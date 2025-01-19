def brute(nums):
    n = len(nums)
    if n == 1:
        return 0
    if n == 2:
        return 0 if nums[0] > nums[1] else 1

    for i in range(1, n-1):
        if nums[i - 1] < nums[i] > nums[i + 1]:
            return i

    if nums[0] > nums[1]:
        return 0
    if nums[n - 1] > nums[n - 2]:
        return n - 1

def optimalBS(arr):
    n = len(arr)
    if n == 1:
        return 0
    if arr[0] > arr[1]:
        return 0
    if arr[n - 1] > arr[n - 2]:
        return n - 1

    low = 1
    high = n - 2
    while low <= high:
        mid = (low + high) // 2
        if arr[mid - 1] < arr[mid] and arr[mid] > arr[mid + 1]:
            return mid
        if arr[mid] > arr[mid - 1]:
            low = mid + 1
        else:
            high = mid - 1

    return -1


print(optimalBS([1,2,1,3,5,6,4]))