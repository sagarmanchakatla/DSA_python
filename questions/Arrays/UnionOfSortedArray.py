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

    return result

calculate([2, 2, 3, 4, 5],[1, 1, 2, 3, 4])