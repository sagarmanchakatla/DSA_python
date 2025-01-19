def brute(nums):
    n = len(nums)

    for i in range(n):
        c = 0
        for j in range(n):
            if nums[i] == nums[j]:
                c += 1
        if c > n/2:
            return nums[i]
        
    return -1



def better(nums):
    h = {}
    for i in nums:
        h[i] = h.get(i, 0) + 1
    
    for key, val in h.items():
        if val > len(nums)/2:
            return key

        

print(brute([3, 3, 4, 2, 4, 4, 2, 4, 4]))

    