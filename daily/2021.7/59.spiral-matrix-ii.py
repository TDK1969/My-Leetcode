class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        answer = []
        for i in range(0, n):
            answer.append([None] * n)

        up = 1
        bottom = n - 1
        left = 0
        right = n - 1
        x = 0
        y = 0
        i = 1
        while True:
            while y <= right:
                answer[x][y] = i
                i += 1
                if i > n * n:
                    return answer
                y += 1
            y -= 1
            right -= 1
            x += 1

            while x <= bottom:
                answer[x][y] = i
                i += 1
                if i > n * n:
                    return answer
                x += 1
            x -= 1
            bottom -= 1
            y -= 1

            while y >= left:
                answer[x][y] = i
                i += 1
                if i > n * n:
                    return answer
                y -= 1
            left += 1
            y += 1
            x -= 1

            while x >= up:
                answer[x][y] = i
                i += 1
                if i > n * n:
                    return answer
                x -= 1
            up += 1
            x += 1
            y += 1