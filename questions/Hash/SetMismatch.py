def brute(nums):
    dup, miss = -1, -1
    for i in range(1, len(nums) + 1):
        count = nums.count(i)
        if count == 2:
            dup = i
        elif count == 0:
            miss = i
    return [dup, miss]

def better(nums):
    n = len(nums)
    dup, miss = -1, -1

    for i in range(1, n+1):
        if i not in nums:
            miss = i
            dup = nums[i-1]
    return [dup, miss]

def optimal(nums):
    n = len(nums)
    h = {}

    for num in nums:
        h[num] = h.get(num, 0) + 1

    miss, dup = -1, -1

    for i in range(1, n + 1):
        if i not in h:
            miss = i
        elif h[i] > 1:
            dup = i

    return [dup, miss]

print(solution([1,2,2,4]))