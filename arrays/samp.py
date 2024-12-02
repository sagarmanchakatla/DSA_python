n = 5
p = 0
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
        p += 1
    if p == n:
       break
    print() 