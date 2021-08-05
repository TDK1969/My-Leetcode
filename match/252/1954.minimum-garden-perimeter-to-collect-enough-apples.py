class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        apples = 0
        r = 1
        while 1:
            temp = (r * (2 * r + 1) + (1 + r) * r - 2 * r) * 4
            apples += temp
            if apples >= neededApples:
                return 8 * r
            r += 1

test = Solution()
print(test.minimumPerimeter(1000000000))