def calculate(nums):
    n = len(nums)
    i = 1

    for j in range(1,len(nums)):
        if nums[j] != nums[j-1]:
            nums[i] = nums[j]
            i += 1
    print(nums)
    return i

print(calculate([0,0,1,1,2,2,3,3]))