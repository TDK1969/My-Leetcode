from collections import Counter
class Solution:
    def originalDigits(self, s: str) -> str:
        s = list(s)
        count = [0 for _ in range(10)]
        number = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
        reflex = {'z': 0, 'x': 6, 'g': 8, 'u': 4, 'f': 5, 'v': 7, 'i': 9, 'n': 1, 'w': 2, 'e': 3}

        chars = Counter(s)

        for alpha, digit in reflex.items():
            while chars[alpha] > 0:
                for a in number[digit]:
                    chars[a] -= 1
                count[digit] += 1

        ans = ""
        for i in range(10):
            ans += str(i) * count[i]

        return ans

test = Solution()
print(test.originalDigits("owoztneoer"))