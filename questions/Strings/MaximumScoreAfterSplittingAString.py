def brute(s):
    n = len(s)
    zero = 0
    one = s.count('1')
    maxi = -1

    for i in range(n-1):
        if s[i] == '0':
            zero += 1
        else:
            one -= 1
        score = zero + one
        maxi = max(maxi, score)
    return maxi

print(brute('1111'))