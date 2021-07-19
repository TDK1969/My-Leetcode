from typing import List
from collections import Counter

class Solution1:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        groups = {}

        for word in strs:
            temp = Counter(word)

            temp2 = tuple(sorted(list(temp.elements())))
            if temp2 in groups:
                groups[temp2].append(word)
            else:
                groups[temp2] = [word]

        for group in groups.values():
            ans.append(group)

        return ans

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        groups = {}

        for word in strs:
            temp2 = sorted(word)
            temp2 = "".join(temp2)
            if temp2 in groups:
                groups[temp2].append(word)
            else:
                groups[temp2] = [word]

        for group in groups.values():
            ans.append(group)

        return ans

test = Solution()
print(test.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))


