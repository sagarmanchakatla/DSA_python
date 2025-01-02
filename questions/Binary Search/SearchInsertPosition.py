def optimal(nums, target):
    n = len(nums)
    low, high = 0, n-1

    while low<=high:
        mid = (low+high)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return low

print(optimal([1,3,5,6], 5))