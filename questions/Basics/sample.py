def reverse( x):
    original = x
    ans = 0
    while x > 0:
        last = x %10 
        ans = ans * 10 + last
        x = int(x / 10)
    print(ans)

# reverse(891)

def calculate(arr):
    n = len(arr)
    if n == 1:
        return 0
    if arr[0] == 0:
        return -1
    
    count = 1
    # jumps = arr[0]

    for i in range(1,n):
        if i == n-1:
            return count
        
        count += 1
        i += arr[i] 

    return count    

# print(calculate([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]))

# print(len(str(153)))

# print([1,2,3,2,1,3].remove(2))

hay = "sadbutsad"

print(hay.find("sad"))