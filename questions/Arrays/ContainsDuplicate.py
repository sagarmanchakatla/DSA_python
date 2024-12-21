def solution(nums):
    n = len(nums)
    h = {}
    for i in range(n):
        h[nums[i]] = h.get(nums[i], 0) + 1
    print(h)
    for key, val in h.items():
        if val > 1:
            return True
    return False
    

print(solution([1, 2, 3, 1]))