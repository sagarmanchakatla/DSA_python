def calculate(nums):
    d = dict()
    for i in nums:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    print(d)
    print(max(d.values()))
    print(d.get)
    print(max(d, key=d.get))

calculate([2,2,1,1,1,1,1,2,2,10,10,10,10,10,10,10])

    