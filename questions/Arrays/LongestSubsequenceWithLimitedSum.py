def solution(nums):
    n = len(nums)
    s = [nums[0]]
    for i in range(1, n):
        s.append(nums[i] + s[-1])
    print(s)
    
solution([1,2,3,4,5])