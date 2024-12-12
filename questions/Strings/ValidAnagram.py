from collections import Counter
class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        h1 = Counter(s)
        h2 = Counter(t)

        return h1==h2