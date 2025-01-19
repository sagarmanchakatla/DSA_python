def fn(i, n):
    return i**n

def brute(n, m):
    for i in range(1, m+1):
        val = fn(i, n)
        if val == m:
            return i
        if val > m:
            break
    return  -1


def optimalBS(n ,m):
    def fn(mid, n, m):
        ans = 1
        for i in range(1, n+1):
            ans *= mid
            if ans > m:
                return 2
        if ans == m:
            return 1
        return 0

    low, high = 0, m

    while low <= high:
        mid =  (low + high) // 2
        val = fn(mid, n, m)
        if val == 1:
            return mid
        elif val == 0:
            low = mid + 1
        else:
            high = mid - 1
    return -1

print(optimalBS(2, 9))