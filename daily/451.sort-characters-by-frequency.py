class Solution:
    def frequencySort(self, s: str) -> str:
        frequency = {}
        ans = ""

        for char in s:
            if char in frequency.keys():
                frequency[char] += 1
            else:
                frequency[char] = 1

        frelist = list(frequency.items())
        frelist.sort(key = lambda x:x[1], reverse=True)

        for char, times in frelist:
            for i in range(times):
                ans += char

        return ans

test = Solution()
print(test.frequencySort("cccaaa"))