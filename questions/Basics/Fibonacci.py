def calculate(n):
    if n <= 1:
        return n
    return calculate(n-1) + calculate(n-2)

def manual(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    sum = 0
    
    for i in range(1,n):
        sum+=1
    
    return sum

print(manual(4))