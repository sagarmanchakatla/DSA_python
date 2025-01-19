def calculate(nums):
    n = len(nums)
    res = int()
    for i in range(n+1):
        if i not in nums:
            res = i
            break

    print(res)

def better(nums):
    hash = [0]*(len(nums)+1)

    for i in range(len(nums)):
        hash[nums[i]] = 1

    for i in range(len(nums)):
        if hash[i] == 0:
            return i
        
def optimal1(nums):
    actual_sum = 0
    for i in nums:
        actual_sum += i
    
    expected_sum = (len(nums) * (len(nums) + 1))/2

    return int(expected_sum - actual_sum)



print(optimal1([9,6,4,2,3,5,7,0,1]))