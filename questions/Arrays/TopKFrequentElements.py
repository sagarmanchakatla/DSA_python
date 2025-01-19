def optimal(nums, k):
    count = {}
    freq = [[] for _ in range(len(nums)+1)]
    
    for i in nums:
        count[i] = count.get(i, 0) + 1
    
    for n, c in count.items():
        freq[c].append(n)
        
    res = []
    for i in range(len(freq)-1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res
            
print(optimal([1,1,1,2,2,3,3,3,3], 2))