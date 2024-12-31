def encode(strs):
    ans = ''
    for s in strs:
        ans += str(len(s)) + '#' + s
    # print(ans)
    return ans

def decode(strs):
    ans = []
    i = 0
    while i < len(strs):
        if strs[i] == '#':
            pass


ans = encode(["lint","code","love","you"])
decode(ans)