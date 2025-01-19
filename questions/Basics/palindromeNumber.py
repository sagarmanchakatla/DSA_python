class Solution(object):
    def isPalindrome(self, x):
        original = x
        ans = 0
        while x > 0:
            last = x % 10
            ans = ans * 10 + last
            x = int(x / 10)
        if ans == original:
            return True
        else: return False
