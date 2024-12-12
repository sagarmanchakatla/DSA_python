from collections import Counter
def frequencySort(s):
    d = Counter(s)
    s = sorted(d.items(), key=lambda x: -x[1])
    ans = ''

    # for i in range(len(d)):

    for i,j in s:
        ans += i *j
    print(s)
    print(ans)

frequencySort('Aabb')