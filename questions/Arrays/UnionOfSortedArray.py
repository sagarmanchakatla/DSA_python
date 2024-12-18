def calculate(a,b):
    n1 = len(a)
    n2 = len(b)
    i = j = 0
    result = []
    
    # Merge two arrays while removing duplicates
    while i < n1 and j < n2:
        if a[i] < b[j]:
            if len(result) == 0 or result[-1] != a[i]:
                result.append(a[i])
            i += 1
        elif a[i] > b[j]:
            if len(result) == 0 or result[-1] != b[j]:
                result.append(b[j])
            j += 1
        else:  # a[i] == b[j]
            if len(result) == 0 or result[-1] != a[i]:
                result.append(a[i])
            i += 1
            j += 1

    # Append remaining elements from a
    while i < n1:
        if len(result) == 0 or result[-1] != a[i]:
            result.append(a[i])
        i += 1

    # Append remaining elements from b
    while j < n2:
        if len(result) == 0 or result[-1] != b[j]:
            result.append(b[j])
        j += 1

    print(result)

def brute(a, b):
    result = set()
    n1 = len(a)
    n2 = len(b)

    for i in range(n1):
        result.add(a[i])
    
    for i in range(n2):
        result.add(b[i])
    
    print(sorted(list(result)))


def optimal(a, b):
    union = []
    i, j = 0, 0

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            if len(union) == 0 or union[-1] != a[i]:
                union.append(a[i])
            i += 1
        else:
            if len(union) == 0 or union[-1] != b[j]:
                union.append(b[j])
            j += 1
    
    while i < len(a):
        if len(union) == 0 or union[-1] != a[i]:
            union.append(a[i])
        i += 1

    while j < len(b):
        if len(union) == 0 or union[-1] != b[j]:
            union.append(b[j])
        j += 1
    
    print(union)

optimal([2, 2, 3, 4, 5],[1, 1, 2, 3, 4])