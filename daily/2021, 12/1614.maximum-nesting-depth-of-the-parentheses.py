class Solution:
    def maxDepth(self, s: str) -> int:
        # stack = []
        maxDepth = 0
        curDepth = 0

        for i in s:
            if i == '(':
                curDepth += 1
                if curDepth > maxDepth:
                    maxDepth = curDepth
            elif i == ')':
                curDepth -= 1

        return maxDepth
