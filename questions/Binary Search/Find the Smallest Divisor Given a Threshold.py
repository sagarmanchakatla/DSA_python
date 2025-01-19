import math

def brute(nums, threshold):
    def calculate(nums, threshold, divisor):
        sum = 0
        for i in range(len(nums)):
           sum += math.ceil(nums[i] / float(divisor))
        if sum <= threshold:
            return True
        else:
            return False

    for i in range(1, max(nums)+1):
        if calculate(nums, threshold, i):
            return i
    return  -1

def optimal(nums, threshold):
    def calculate(nums, threshold, divisor):
        sum = 0
        for i in range(len(nums)):
            sum += math.ceil(nums[i] / float(divisor))
        if sum <= threshold:
            return True
        else:
            return False

    maxi = max(nums)
    low, high = 1, maxi

    while low <= high:
        mid = (low + high) // 2
        if calculate(nums, threshold, mid):
            high = mid - 1
        else:
            low = mid + 1
    return low

print(brute([44,22,33,11,1], 5))