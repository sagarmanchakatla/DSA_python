class Solution(object):
    def reverse(self, x):
        original = x
        ans = 0
        isNeg = x < 0
        x = abs(x)
        while x > 0:
            last = x %10 
            ans = ans * 10 + last
            x = int(x / 10)
        if isNeg:
            ans = -ans
        if ans < -2**31 or ans > 2**31 - 1:
            return 0
        return ans
        
        