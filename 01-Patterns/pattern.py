def print1(n):
    for i in range(n):
        for i in range(n):
            print("*",end='')
        print()
def print2(n):
    for i in range(1,n):
        for j in range(1,i+1):
            print('*',end='')
        print()
def print3(n):
    for i in range(1,n):
        for j in range(1,i+1):
            print(j,end='')
        print()
def print4(n):
    for i in range(1,n):
        for j in range(1,i+1):
            print(i,end='')
        print()
def print5(n):
    for i in range(1,n+1):
        for j in range(0,n-i+1):
            print('*',end="")
        print()
def print6(n):
    for i in range(0,n+1):
        for j in range(1,n-i+1):
            print(j,end="")
        print()
def print7(n):
    for i in range(n):
        for j in range(n-i-1):
            print(' ',end=' ')
        for j in range(2*i+1):
            print('*',end=' ')
        for j in range(n-i-1):
            print(' ',end=' ')
        print()
def print8(n):
    for i in range(n):
        for j in range(i):
            print(' ',end=' ')
        for j in range(2*n-1-i*2):
            print('*',end=' ') 
        for j in range(i):
            print(' ',end=' ')
        print()      
def print9(n):
    print7(n)
    print8(n)

def print10(n):
    for i in range(n):
        for j in range(i+1):
            print('*',end='')
        for j in range():
            pass

def print11(n):
    start = 1
    for i in range(1,n+1):
        for j in range(i):
            print(start, end=' ')
            if start == 1 : start = 0
            else : start = 1
        print()   

def print12(n):
    spaces = 2*(n-1)
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j, end=' ')
        for j in range(spaces+1):
            print(' ', end=' ')
        for j in range(i,0,-1):
            print(j, end=' ')
        print()
        spaces -= 2

def print13(n):
    step = 1
    for i in range(n):
        for j in range(i+1):
            print(step, end=' ')
            step += 1
        print()

def print14(n):
    for i in range(n):
        for j in range(i+1):
            print(chr(65+j), end=' ')
        print()

print14(4)