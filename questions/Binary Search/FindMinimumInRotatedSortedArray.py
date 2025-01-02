import sys

def brute(nums):
    ans = sys.maxsize
    for i in range(len(nums)):
        ans = min(ans, nums[i])
    return ans


def optimal(nums):
    n = len(nums)
    ans = sys.maxsize
    low, high = 0, n - 1
    min = -1
    while low <= high:
        mid = (low + high) // 2

        # left half sorted ??
        if nums[low] <= nums[mid]:
            if nums[low] < ans:
                ans = nums[low]
                min = low
            # ans = min(ans, nums[low])
            low = mid + 1
        else:
            if nums[mid] < ans:
                ans = nums[mid]
                min = mid
            # ans = min(ans, nums[mid])
            high = mid - 1
    return min

print(optimal([10,11,13,15,17,9]))