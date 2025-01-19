import sys
def brute(nums):
    maxs = -sys.maxsize - 1
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            s = 0
            for k in range(i, j+1):
                s += nums[k]
            maxs = max(maxs, s)

    return maxs


def better(nums):
    maxs = 0
    for i in range(len(nums)):
        s = 0
        for j in range(i, len(nums)):
            s += nums[j]
            maxs = max(maxs, s)

    return maxs



def optimal(nums):
    maxs = -sys.maxsize - 1
    sum = 0
    for i in range(len(nums)):
        sum += nums[i]

        if sum > maxs:
            maxs = sum 

        if sum < 0:
            sum = 0

        
def printTheSubArray(nums):
    maxs = -sys.maxsize-1
    start = 0
    sum = 0
    arrS, arrE = -1, -1

    for i in range(len(nums)):
        sum += nums[i]
        if sum == 0:
            start = i

        if sum > maxs:
            maxs = sum
            arrS = start
            arrE = i

        if sum < 0:
            sum = 0
    
    
         

print(brute([-2,1,-3,4,-1,2,1,-5,4]))