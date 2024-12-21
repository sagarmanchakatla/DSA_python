from collections import Counter

def isAnagram(s, t):
    if len(s) != len(t):
        return False

    h1 = Counter(s)
    h2 = Counter(t)

    return h1==h2

def brute(s, t):
    if len(s) != len(t):
        return False

    hashmap = {}
    for i in s:
        hashmap[i] = hashmap.get(i, 0) + 1
    
    for i in t:
        if i not in hashmap or hashmap[i] == 0:
            return False
        else:
            hashmap[i] -= 1
        
    return True 