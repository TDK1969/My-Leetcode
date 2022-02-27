from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        c1 = Counter(s)
        c2 = Counter(t)
        ans = 0

        for i in range(26):
            temp = chr(ord('a') + i)
            ans += abs(c1[temp] - c2[temp])

        return ans