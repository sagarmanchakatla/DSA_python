def isPalindrome(s: str) -> bool:
    st = ''.join(char.lower() for char in s if char.isalnum())
    print(st)
    n = len(st)
    low, high = 0, n - 1
    while low <= high:
        if st[low] == st[high]:
            low += 1
            high -= 1
        else:
            return False
    return True

print(isPalindrome("Was it a car or a cat I saw?"))