def hash():
    n = int(input('Enter the size of array: '))
    arr = [0] * n

    for i in range(n):
        arr[i] = input(f'Enter the {i+1} element(capital): ')

    hash = [0] * 256

    for i in range(n):
        hash[ ord(arr[i]) ] += 1
    
    q = int(input('Enter the number of queries: '))

    while q:
        r = input('Enter the character: ')
        print(f'{r} occurs {hash[ord(r)]} times in the array')
        q -= 1

if __name__ == '__main__':
    hash()