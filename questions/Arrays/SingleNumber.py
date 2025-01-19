def calculate(nums):
    d = {}
    for i in nums:
        d[i] = d.get(i, 0) + 1

    for i in d.items():
        if i[1] == 1:
            return i[0]

def brute(nums):
    for i in range(len(nums)):
        num = nums[i]
        count = 0
        for j in range(len(nums)):
            if nums[j] == num:
                count += 1
        if count == 1:
            return num
            
print(brute([4,4,5,1,2,1,2]))


