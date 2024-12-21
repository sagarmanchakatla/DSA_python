def brute1(arr, k):
    maxl = 0
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            s = 0
            for l in range(i, j+1):
                s += arr[l]
            if s == k:
                maxl = max(maxl, i-j+1)
    print(maxl)

def brute2(arr, k):
    maxl = 0
    for i in range(len(arr)):
        s = 0
        for j in range(i, len(arr)):
            s += arr[j]
            if s == k:
                maxl = max(maxl, j-i+1)

    print(maxl)

def better(arr, k):
    prefixSum = 0
    maxl = 0
    hashmap = {}

    for i in range(len(arr)):
        prefixSum += arr[i]
        if prefixSum == k:
            maxl = max(maxl, i+1)

        pre = prefixSum - k
        if pre in hashmap:
            maxl = max(maxl, i-hashmap[pre])
        
        if prefixSum not in hashmap:
            hashmap[prefixSum] = i
    
    print(maxl)


def optimal(arr, k):
    left = right = 0
    maxsum = arr[0]
    maxl = 0
    n = len(arr)

    while right < n:
        while left <= right and maxsum > k:
            maxsum -= arr[left]
            left += 1
        if maxsum == k:
            maxl = max(maxl, right-left+1)
        right += 1
        if right < n:
            maxsum += arr[right]

    print(maxl)

optimal([10, 5, 2, 7, 1, 9],15)

