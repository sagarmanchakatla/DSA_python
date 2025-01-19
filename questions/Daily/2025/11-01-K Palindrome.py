from collections import Counter

def solution(s, k):
    if len(s) < k:
        return False

    char_count = Counter(s)
    summ = sum(freq % 2 for freq in char_count.values())
    return summ <= k

print(solution("abc", 2))