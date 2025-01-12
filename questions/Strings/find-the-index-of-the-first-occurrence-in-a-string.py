def brute(haysack, needle):
    for i in range(len(haysack) - len(needle) + 1):
        if haysack[i: i+len(needle)] == needle:
            return i
    return -1