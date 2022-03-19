from typing import List
class Solution:
    def longestWord(self, words: List[str]) -> str:
        wordsSet = set(words)
        words = list(wordsSet)
        words.sort(key=lambda x:[-len(x), x])
        for word in words:
            flag = False
            if len(word) == 1:
                return word
            for i in range(len(word) - 1, 0, -1):
                if word[:i] not in wordsSet:
                    flag = False
                    break
                flag = True
            if flag:
                return word
        return ""

test = Solution()
print(test.longestWord(["e"]))