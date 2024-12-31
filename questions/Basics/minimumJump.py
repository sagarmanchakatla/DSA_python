def calculate(arr):
    n = len(arr)
    if n == 1:
        return 0
    if arr[0] == 0:
        return -1
    
    current = 0
    maxR = 0
    count = 0

    for i in range(n):
        maxR = max(maxR, i+arr[i]) 
        
        if i == current:
            count += 1
            current += maxR

            if current >= n-1:
                return count
        
        if maxR <= i:
            return -1
    return -1

print(calculate([0, 10, 20]))
