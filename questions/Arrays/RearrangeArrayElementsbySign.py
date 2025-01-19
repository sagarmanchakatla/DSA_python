def brute(nums):
    pos = []
    neg = []
    ans = [0]*len(nums)
    j, k = 0, 0
    for i in nums:
        if i >= 0:
            pos.append(i)
        else:
            neg.append(i)
    
    for i in range(len(nums)):
        if i % 2 == 0:
            ans[i] = pos[j]
            j += 1
        else:
            ans[i] = neg[k]
            k += 1
    print(ans)



def solution(nums):
    j, k = 0, 1
    ans = [0]*len(nums)
    for i in range(len(nums)):
        if nums[i] >= 0:
            ans[j] = nums[i]
            j += 2
        else:
            ans[k] = nums[i]
            k += 2
    print(ans)

brute([-1,1])