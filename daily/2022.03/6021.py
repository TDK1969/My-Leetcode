class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        if pattern[0] == pattern[1]:
            count = text.count(pattern[0])
            return (count + 1) * count // 2

        count0 = 0
        count1 = 0
        countPattern = 0


        for char in text:
            if char == pattern[0]:
                count0 += 1
            if char == pattern[1]:
                count1 += 1
                countPattern += count0

        return countPattern + max(count0, count1)
