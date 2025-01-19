def brute(temperatures):
    n = len(temperatures)
    res = []
    
    for i in range(n):
        j = i + 1
        count = 1
        while j < n:
            if temperatures[j] > temperatures[i]:
                break
            count += 1
            j += 1
        count = 0 if j == n else count
        res.append(count)
    
    return res

def better(temperatures):
    n = len(temperatures)
    res = [0] * n
    stack = []
    
    for index, temp in enumerate(temperatures):
        while stack and temp > stack[-1][0]:
            stack_temp, stack_index = stack.pop()
            res[stack_index] = index - stack_index
        stack.append((temp, index))
    
    return res