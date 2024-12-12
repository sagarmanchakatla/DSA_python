def calculate(s):
    words = s.split()
    words.reverse()
    return ' '.join(words)

print(calculate("  hello world  "))