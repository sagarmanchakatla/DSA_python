def calculate(arr):
    d = dict()
    for i in arr:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    
    return list(d.values())
print(calculate([2, 3, 2, 3, 5]))