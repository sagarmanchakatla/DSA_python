def calculate(nums):
    n = len(nums)
    res = int()
    for i in range(n+1):
        if i not in nums:
            res = i
            break

    print(res)

calculate([9,6,4,2,3,5,7,0,1])