def brute(bloomDay, m, k):
    def isPossible(bloomDay, day, m, k):
        count = 0
        noOfB = 0

        for i in range(len(bloomDay)):
            if bloomDay[i] <= day:
                count += 1
            else:
                noOfB += count // k
                count = 0
        noOfB += count // k
        return noOfB >= m

    mini = min(bloomDay)
    maxi = max(bloomDay)

    val = m * k
    if len(bloomDay) < val:
        return -1

    for i in range(mini, maxi+1):
        if isPossible(bloomDay, i, m, k):
            return i
    return -1


def optimalBS(bloomDay, m, k):
    def isPossible(bloomDay, day, m, k):
        count = 0
        noOfB = 0

        for i in range(len(bloomDay)):
            if bloomDay[i] <= day:
                count += 1
            else:
                noOfB += count // k
                count = 0
        noOfB += count // k
        return noOfB >= m

    mini = min(bloomDay)
    maxi = max(bloomDay)

    val = m * k
    if len(bloomDay) < val:
        return -1

    low, high = mini, maxi

    while low <= high:
        mid = (low + high) //2
        if isPossible(bloomDay, mid, m, k):
            high = mid - 1
        else:
            low = mid + 1
    return low