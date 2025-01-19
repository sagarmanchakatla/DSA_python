def brute(A, B):
    n = len(A)
    res = [0] * n
    setA, setB = set(), set()
    
    for i in range(n):
        count = 0
        
        setA.add(A[i])
        setB.add(B[i])
        
        for j in setA:
            if j in setB:
                count += 1
            
        res[i] = count
    
    return res

print(brute([1,3,2,4], [3,1,2,4]))


def better(A, B):
    n = len(A)
    res = [0] * n
    freq = [0] * (n+1)
    
    count = 0
    for i in range(n):
        
        freq[A[i]] += 1
        if freq[A[i]] == 2:
            count += 1
        freq[B[i]] += 1
        if freq[B[i]] == 2:
            count += 1
            
        res[i] = count

    return res


print(better([1,3,2,4], [3,1,2,4]))