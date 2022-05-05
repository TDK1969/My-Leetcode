from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        alpha_dict = [0 for _ in range(26)]
        p, q = 0, 0
        max_len = 0

        while q < len(s):
            alpha_dict[ord(s[q]) - 65] += 1
            while max(alpha_dict) + k < q - p + 1:
                alpha_dict[ord(s[p]) - 65] -= 1
                p += 1
            max_len = max(max_len, q - p + 1)
            q += 1
 
        max_len = max(max_len, q - p)
        return max_len

test = Solution()
print(test.characterReplacement(s = "ABAB", k = 2))
               

