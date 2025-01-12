def brute(nums):
    n = len(nums)
    count = 0
    totalSum = sum(nums)
    leftSum = 0
    rightSum = 0

    for i in range(n-1):
        leftSum += nums[i]
        rightSum = totalSum - leftSum
        if leftSum > rightSum:
            count += 1

    return count

print(brute([0,0]))