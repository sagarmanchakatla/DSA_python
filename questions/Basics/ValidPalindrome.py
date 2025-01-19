def calculate(s):
    ans = ''.join(ch.lower() for ch in s if ch.isalnum())
    print(ans)
    print(ans[::-1])
    if ans == ans[::-1]:
        return True
    else: False

print(calculate('race a car'))