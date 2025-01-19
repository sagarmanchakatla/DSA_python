def calculate(s,k):
    sol = []
    for i in range(len(s)+1):
        for j in range(i+1,k+1):
            sol.append(s[i:j])
    
    print(sol)

calculate('abc',2)

print(1 // 2)