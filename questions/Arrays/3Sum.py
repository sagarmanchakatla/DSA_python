def brute(nums):
    n = len(nums)
    res = set()

    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    tmp = [nums[i], nums[j], nums[k]]
                    tmp.sort()
                    res.add(tuple(tmp))
    return [list(i) for i in res]
        

def better(nums):
    n = len(nums)
    res = set()
    
    for i in range(n):
        hashset = set()
        for j in range(i+1, n):
            third = -(nums[i] + nums[j])
            
            if third in hashset:
                temp = [nums[i], nums[j], third]
                temp.sort()
                res.add(tuple(temp))
            hashset.add(nums[j])

    return list(res)    

def optimal(nums):
    nums.sort()
    n = len(nums)
    res = []
    
    for i in range(n):
        if i != 0 and nums[i] == nums[i-1]:
            continue
        
        j = i + 1
        k = n - 1
        
        while j < k:
            total_sum = nums[i] + nums[j] + nums[k]
            if total_sum < 0:
                j += 1
            elif total_sum > 0:
                k -= 1
            else:
                res.append([nums[i], nums[j], nums[k]])
                j += 1
                k -= 1
            
                while j < k and nums[j] == nums[j-1]:
                    j += 1
                while j < k and nums[k] == nums[k+1]:
                    k -= 1
                
                    
    
    return res     
        
print(brute([-1,0,1,2,-1,-4]))
