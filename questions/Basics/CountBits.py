def calculate(n):
    ans = []

    for i in range(n+1):
        ans.append(bin(i)[2:].count('1'))

    print(ans)

calculate(5)