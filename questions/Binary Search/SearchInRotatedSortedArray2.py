def brute(nums, target):
    n = len(nums)
    for i in range(n):
        if nums[i] == target:
            return i

def optimal(nums, target):
    n = len(nums)
    low, high = 0, n-1

    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target: return mid

        if nums[low] == nums[mid] == nums[high]:
            low += 1
            high -= 1
            continue

        # left half sorted ??
        if nums[low] <= nums[mid]:
            if nums[low] <= target <= nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        # right half sorted ??
        else:
            if nums[mid] <= target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1


print(optimal([1,0,1,1,1], 0))