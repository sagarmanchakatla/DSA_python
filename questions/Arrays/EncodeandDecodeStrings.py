def encode(strs):
    ans = ''
    for i in strs:
        ans += str(len(i)) + '#' + i
    return ans


def decode(s):
    ans = []
    i = 0
    while i < len(s):
        # Find the delimiter '#'
        j = s.find('#', i)
        # Extract the length of the string
        length = int(s[i:j])
        # Extract the string based on the length
        ans.append(s[j + 1:j + 1 + length])
        # Move the pointer forward
        i = j + 1 + length
    return ans

ans = encode(["lint","code","love","you"])
s = encode(["lint","code","love","you"])
print(ans)
print(decode(ans))