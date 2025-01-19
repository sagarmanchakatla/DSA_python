def frequencyCount( arr):
    n = len(arr)
    print(n)
    hash = [0] * (n)
    print(hash)

    for i in range(n):
        print(arr[i])
        hash[arr[i]-1] += 1
        
    return hash

print(frequencyCount([2, 3, 2, 3, 5]))