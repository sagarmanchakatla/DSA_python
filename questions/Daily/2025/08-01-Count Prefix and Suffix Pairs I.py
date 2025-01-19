class Solution(object):

    def isPrefixAndSuffix(self, str1, str2):
        n1, n2 = len(str1), len(str2)

        if n1 > n2:
            return False
        if str2[:n1] == str1 and str2[-n1:] == str1:
            return True
        else:
            return False

    def countPrefixSuffixPairs(self, words):
        n = len(words)
        count = 0
        for i in range(n):
            for j in range(i + 1, n):
                if self.isPrefixAndSuffix(words[i], words[j]):
                    count += 1
        return count
