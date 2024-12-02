def hash():
    n = int(input('Enter the size of array: '))
    arr = [0] * n

    for i in range(n):
        arr[i] = int(input(f'Enter the {i+1} element: '))   
    
    hash = [0] * 13

    for i in range(n):
        hash[arr[i]] += 1

    q = int(input('Enter the number of queries: '))

    while q:
        r = int(input('Enter the number: '))
        print(f'{r} occurs {hash[r]} times in the array')
        q -= 1

if __name__ == '__main__':
    # hash()
    s = 'Hello World'
    print(s[2])