class Solution(object):
    def minOperations(self, boxes):
        n = len(boxes)
        res = [0] * n

        for i in range(n):
            operation = 0
            for j in range(n):
                if boxes[j] == '1':
                    operation += abs(j - i)
            res[i] = operation

        return res