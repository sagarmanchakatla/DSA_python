def calculate(n):
    sum = 0
    for i in range(1,n+1):
        multiples = n// i
        print(i,multiples)
        sum += multiples*i
    return sum

print(calculate(4))