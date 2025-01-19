def calculate(nums, target):
    l,h = 0, len(nums)
        
    while l<h:
        m = (l+h) // 2
        if target < nums[m]:
            h = m - 1
        elif target > nums[m]:
            l = m +1
        else:
            return m
    return l

print(calculate([1,3],2))