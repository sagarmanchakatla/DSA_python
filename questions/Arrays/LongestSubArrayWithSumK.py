def approach1(nums,K):
    maxL = 0
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            sum = 0
            for k in range(i,j):
                sum += nums[k]
            if sum == K:
                maxL = max(maxL, j-i)

    print(maxL)

approach1([10, 5, 2, 7, 1, 9],15)


def approch2(nums,K):
    maxL = 0
    for i in range(len(nums)):
        sum = 0
        for j in range(i,len(nums)):
            sum += nums[j]
            if sum == K:
                maxL = max(maxL, j-i)
    print(maxL)

approch2([10, 5, 2, 7, 1, 9],15)
