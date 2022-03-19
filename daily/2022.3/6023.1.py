class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        numFloor = []
        remainWhite = 0
        for i in floor:
            if i == '0':
                numFloor.append(0)
            if i == '1':
                remainWhite += 1
                numFloor.append(1)

        n = len(floor)

        while numCarpets:
            numCarpets -= 1
            index = -1
            maxCount = -1

            for i in range(0, n - carpetLen + 1):
                whiteCount = sum(numFloor[i:i + carpetLen])
                if whiteCount > maxCount:
                    maxCount = whiteCount
                    index = i

            if maxCount == 0:
                return 0

            remainWhite -= min(maxCount, carpetLen)
            for i in range(index, index + carpetLen):
                numFloor[i] = 0

        return remainWhite

test = Solution()
print(test.minimumWhiteTiles("101111"
,2
,3))