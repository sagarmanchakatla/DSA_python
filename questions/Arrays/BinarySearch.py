def calculate(nums, target):
    nums.sort()
    l, h = 0, len(nums)-1

    while l <= h:
        m = (l+h)//2
        # print(m)
        if nums[m] == target:
            return m
        elif nums[m] < target:
            l = m+1
        else:
            h = m-1
    return -1

    
print(calculate([-1,0,3,5,9,12],9))
