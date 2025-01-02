def brute(arr):
    h = {}
    for i in range(len(arr)):
        h[arr[i]] = h.get(arr[i], 0) + 1

    for n, c in h.items():
        if c == 1:
            return n


def binary(nums):
    n = len(nums)
    if n == 1:
        return nums[0]
    if nums[0] != nums[1]:
        return nums[0]
    if nums[n-1] != nums[n-2]:
        return nums[n-1]

    low, high = 1, n-2
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1]:
            return nums[mid]

        if (mid%2 == 1 and nums[mid-1] == nums[mid]) or (mid%2 == 0 and nums[mid+1] == nums[mid]):
            low = mid + 1
        else:
            high = mid - 1



print(binary([1,1,2,3,3,4,4,8,8]))