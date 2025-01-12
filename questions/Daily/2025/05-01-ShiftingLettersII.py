def brute(s, shifts):
    m = len(shifts)
    
    res = [ord(c) - ord('a') for c in s]

    for i in range(m):
        for j in range(shifts[i][0], shifts[i][1]+1):
            if shifts[i][2] == 0:
                res[j] = ((res[j] - 1)+26)%26
            else:
                res[j] = ((res[j] + 1)+26)%26
        print(res)
    
    st = ''
    for i in res:
        st += chr(ord('a') + i)
    
    return st

print(brute('abc', [[0,1,0],[1,2,1],[0,2,1]]))