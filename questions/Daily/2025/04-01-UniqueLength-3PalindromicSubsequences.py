def brute(s):
    res = set()
    n = len(s)
    
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if s[i] == s[k]:
                    res.add((s[i], s[j]))
    
    return len(res)

from collections import Counter
def optimal(s):
    res = set()
    left = set()
    right = Counter(s)
    
    for m in s:
        right[m] -= 1
        for c in left:
            if right[c] > 0:
                res.add((c, m))
        left.add(m)
    
    return len(res)
    
        int: The count of unique palindromic subsequences of length 3.
    """

