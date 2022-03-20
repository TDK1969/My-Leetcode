from typing import List


class Solution:
    def num0fStrings(self, patterns: List[str], word: str) -> int:
        ans = 0
        for s in patterns:
            if s in word:
                ans += 1
        return ans