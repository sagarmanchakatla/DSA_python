def brute(weights, days):
    def findCap(wt, days, cap):
        load = 0
        day = 1

        for i in range(len(wt)):
            if (load + wt[i]) > cap:
                day += 1
                load = wt[i]
            else:
                load += wt[i]
        if day <= days:
            return True
        else:
            return False

    maxi = max(weights)
    sumi = sum(weights)

    for i in range(maxi, sumi):
        if findCap(weights, days, i):
            return i
    return -1

print(brute( [3,2,2,4,1,4], 3))