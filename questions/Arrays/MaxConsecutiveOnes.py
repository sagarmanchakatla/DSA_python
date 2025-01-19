def calculate(nums):
    maxi = 0
    count = 0

    for i in range(len(nums)):
        if nums[i] == 1:
            count += 1
            maxi = max(maxi,count)
        else:
            count = 0

    return maxi
        
print(calculate([1,0,1,1,0,1]))