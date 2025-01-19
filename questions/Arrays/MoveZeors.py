def calculate(nums):
    i = 0

    for j in range(len(nums)):
        if nums[j] != 0:
            nums[i] = nums[j]
            i += 1
    
    for k in range(i, len(nums)):
        nums[k] = 0

    print(nums)


def brute(nums):
    temp = []

    for i in nums:
        if i != 0:
            temp.append(i)
    
    i = 0

    for j in range(len(temp)):
        nums[i] = temp[j]
        i += 1
    
    for k in range(i, len(nums)):
        nums[k] = 0
    
    print(nums)

brute([0,1,0,3,12])