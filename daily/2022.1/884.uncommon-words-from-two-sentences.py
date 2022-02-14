from typing import List
from collections import Counter

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1 = s1.split()
        s2 = s2.split()
        w1 = Counter(s1)
        w2 = Counter(s2)
        words1 = set(s1)
        words2 = set(s2)
        ans = []
        for word in s1:
            if w1[word] == 1 and word not in words2:
                ans.append(word)
        for word in s2:
            if w2[word] == 1 and word not in words1:
                ans.append(word)
        return ans

test = Solution()
print(test.uncommonFromSentences(s1 = "s z z z s", s2 = "s z ejt"))