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
    
def optimalSolution(arr):
    n = len(arr)
    ans = []
    max_ele = arr[n-1]
    ans.append(max_ele) # last element is always the leader

    for i in range(n-2, -1, -1):
        if arr[i] > max_ele:
            max_ele = arr[i]
            ans.append(max_ele)

    print(*ans)
solution([10, 4, 2, 4, 1])