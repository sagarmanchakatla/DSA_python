from collections import Counter

def solution(words1, words2):
    counter = Counter(words2)
    res = []
    for i in words1:
        flag = False
        for j in i:
            if j in words2:
                counter[j] -= 1
                flag = True
        for val in counter.values():
            if val == 0:
                flag = True
            else:
                flag = False
        if flag:
            res.append(i)
        counter = Counter(words2)

    print(res)
    
    
solution(["amazon","apple","facebook","google","leetcode"], ["e","o"])