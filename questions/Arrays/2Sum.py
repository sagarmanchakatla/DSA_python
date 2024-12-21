def brute1(arr, target):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i == j: continue
            if arr[i]+arr[j] == target:
                return [i,j]

def brute2(arr, target):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
                return [i,j]


def better(arr, target):
    hashmap = {}
    
    for i in range(len(arr)):
        pre = target - arr[i]
        if pre in hashmap:
            return [hashmap[pre], i]
        hashmap[arr[i]] = i

def optimal(arr, target):
    left, right = 0, len(arr)-1
    arr.sort()

    while left < right:
        s = arr[left] + arr[right]
        if s < target:
            left += 1
        elif s > target:
            right -= 1
        else:
            return [left, right]

print(optimal([3,2,3], 6)) 

