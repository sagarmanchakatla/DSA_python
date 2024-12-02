def printName(i,n):
    if i > n:
        return
    print('Sagar')
    printName(i+1,n)

# printName(1,5)

def printLinearNumber(i,n):
    if i > n:
        return
    print(i)
    printLinearNumber(i+1,n)

# printLinearNumber(1,5)

def printLinearNumberReverse(n):
    if n < 0:
        return 
    print(n)
    printLinearNumberReverse(n-1)

# printLinearNumberReverse(10)

def oneToNBacktrack(i,n):
    if i<1:
        return
    oneToNBacktrack(i-1,n)
    print(i)

# oneToNBacktrack(5,5)

def NtoOneBacktrack(i,n):
    if i==0:
        return
    print(i)
    NtoOneBacktrack(i-1,n)

# NtoOneBacktrack(5,5)

def SumofN(i,sum):
    if i < 1:
        print(sum)
        return 
    SumofN(i-1,sum+i)

# SumofN(3,0)    

def sumN(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return n + sumN(n-1)

# print(sumN(5))

def factorial(n):
    if n == 0: return 0
    if n == 1: return 1
    return n * factorial(n-1)

# print(factorial(4))

def reverseArray(arr):
    L = 0
    R = len(arr)-1
    while L < R:
        arr[L], arr[R] = arr[R], arr[L]
        L+=1
        R-=1

def reverseArrayRecursion(l,r):
    if l >= r: return
    arr[l],arr[r] = arr[r],arr[l]
    reverseArrayRecursion(l+1,r-1)

# def reverse(i):
    # if i >= len(arr)

    
arr = [1,2,3,3,4,1]
# reverseArray(arr)
# reverseArrayRecursion(0,len(arr)-1)
print(arr)