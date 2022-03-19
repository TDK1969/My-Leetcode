import heapq


class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        white = []
        heapq.heapify(white)

        whiteBlock = floor.split('0')
        for block in whiteBlock:
            heapq.heappush(white, -len(block))

        while numCarpets:
            numCarpets -= 1
            if white:
                temp = -heapq.heappop(white)
                if temp > carpetLen:
                    heapq.heappush(white, temp - carpetLen)
            else:
                return 0
        return sum(white)

test = Solution()
print(test.minimumWhiteTiles("0010000101101001111010010101110001100111000010100011111011100101011000111101001000010011010"
,22
,19))