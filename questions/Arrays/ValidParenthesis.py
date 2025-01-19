def solution(s):
    stack = []
    open = {'(':')',
            '{':'}',
            '[':']'
            }

    for c in s: 
        if c in open.keys():
            stack.append(c)
        else:
            if c in open.values():
                if not stack or open[stack.pop()] != c:
                    return False

    return True if not stack else False

print(solution("(]"))