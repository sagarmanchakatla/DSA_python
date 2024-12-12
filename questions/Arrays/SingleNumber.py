def calculate(nums):
    d= dict()
    for i in nums:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    for i in d.items():
        if i[1] == 1:
            print(i[0])
            
calculate([4,1,2,1,2])