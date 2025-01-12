import math

def getTotalHours(piles, hour):
    totalTime = 0
    for i in range(len(piles)):
        totalTime += math.ceil(float(piles[i] / hour))
    return totalTime

def brute(piles, h):
    for i in range(max(piles)):
        reqtime = getTotalHours(piles, i)
        if reqtime <= h:
            return i

def optimal(piles, h):
    low, high = 0, max(piles)

    while low <= high:
        mid = (low + high) // 2
        totalHours = getTotalHours(piles, mid)
        if totalHours <= h:
            high = mid - 1
        else:
            low  = mid + 1
    return low