def calculate(n):
    sum = 0
    for i in range(len(str(n))):
        x = n % 10
        sum += x**3
        n = int(n / 10)
    
    if sum == n:
        print("Armstrong Number")
    else:
        print("Not Armstrong Number")

calculate(153)