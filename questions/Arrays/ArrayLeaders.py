def solution(nums):
    n = len(nums)
    ans = []
    
    for i in range(n):
        for j in range(i+1,n):
            if nums[j] > nums[i]:
                break
        else:
            ans.append(nums[i])
    
    print(ans)
    
solution([16, 17, 4, 3, 5, 2])