def calculate(nums):
    index = len(nums)-1
    l,r = 0, len(nums)-1
    result = [0]*len(nums)
    while l < r:
        l1 = nums[l]**2
        r1 = nums[r]**2

        if l1 >= r1:
            result[index] = l1
            l+=1
        else:
            result[index] = r1
            r-=1
        index-=1
    return result

print(calculate([-4,-1,0,3,10]))