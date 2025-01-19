import sys

def brute(arr):
    
    def ls(arr,x):
        for i in range(len(arr)):
            if arr[i] == x:
                return True
        return False
    
    n = len(arr)
    longest = 1

    for i in range(n):
        x = arr[i]
        count = 1
        while ls(arr,x+1):
            x += 1
            count += 1
        longest = max(longest, count)
    return longest


def better(arr):
    n = len(arr)
    longest = 1
    lastSmaller = -sys.maxsize - 1
    count = 0

    for i in range(n):
        if arr[i]-1 == lastSmaller:
            count += 1
            lastSmaller = arr[i]
        elif lastSmaller != arr[i]:
            count = 1
            lastSmaller = arr[i]

        longest = max(longest, count)
    return longest


def optimal(arr):
    n = len(arr)
    if n == 0: return 0

    st = set()
    for i in arr:
        st.add(i)

    longest = 1
    for it in st:
        if it-1 not in st:
            count = 1
            x = it
            while x+1 in st:
                count += 1
                x += 1
            longest = max(longest, count)
    
    return longest



print(optimal([100,101,4,200,2,102]))