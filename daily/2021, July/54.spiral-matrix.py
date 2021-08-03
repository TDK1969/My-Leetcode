class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        answer = []
        a = len(matrix)
        b = len(matrix[0])

        for times in range(0, a):
            matrix[times].append(None)
            matrix[times].insert(0, None)
        temp = [None] * (b + 2)
        matrix.insert(0, temp)
        matrix.append(temp)

        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        direct = 0
        i = 1
        j = 1
        count = 0

        while count < a * b:
            answer.append(matrix[i][j])
            count += 1
            matrix[i][j] = None
            if matrix[i + direction[direct][0]][j + direction[direct][1]] == None:
                direct += 1
                direct %= 4
            i = i + direction[direct][0]
            j = j + direction[direct][1]
        return answer