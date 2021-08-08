from typing import List


class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        pre = ""
        for word in words:
            pre += word
            if pre == s:
                return True
        return False

test = Solution