class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if set(s) != set(goal):
            return False
        n = len(s)
        for i in range(n):
            if s[0 : i] == goal[n - i : n] and s[i : n] == goal[0 : n - i]:
                return True
        return False

test = Solution()
print(test.rotateString(s = "gcmbf", goal = "fgcmb"))