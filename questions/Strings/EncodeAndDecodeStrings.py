def encode(strs):
    res = ''
    for s in strs:
        res += str(len(s)) + '#' + s
    return res

def decode(str):
    n = len(str)
    res = []
    i = 0

    while i < n:
        j = i
        while str[j] != '#':
            j += 1
        length = int(str[i:j])
        res.append(str[j+1 : j+1+length])
        i = j+1+length
    return res

encoded = encode(['neet', 'codes'])
decoded = decode(encoded)
print('Encoded String', encoded)
print('Decoded String', decoded)