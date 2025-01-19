class Solution(object):
    def prefixCount(self, words, pref):
        count = 0

        for i in words:
            if i[:len(pref)] == pref:
                count += 1
            # if i.startswith(pref):
            #     count += 1
        return count
