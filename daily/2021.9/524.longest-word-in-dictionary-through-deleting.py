from typing import List
import heapq

class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        ans = []
        maxlen = -1
        for word in dictionary:
            i, j = 0, 0
            while i < len(word) and j < len(s):
                if word[i] == s[j]:
                    i += 1
                j += 1
            if i == len(word):
                if i > maxlen:
                    ans.clear()
                    maxlen = i
                if i == maxlen:
                    heapq.heappush(ans, word)
        if not ans:
            return ""
        return heapq.heappop(ans)

    def findLongestWordSort(self, s: str, dictionary: List[str]) -> str:
        dictionary.sort(key=lambda x:(-len(x), x))
        # 对dictionary排序进行预处理，按照长度非升序，字典序非降序排序
        # 这样找到的第一个一定是长度最长而且字典序最小的
        for word in dictionary:
            i, j = 0, 0
            while i < len(word) and j < len(s):
                if word[i] == s[j]:
                    i += 1
                j += 1
            if i == len(word):
                return word
        return ""


test = Solution()
print(test.findLongestWordSort(s = "abpcplea", dictionary = ["ale","apple","monkey","plea"]))

