from typing import List


class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        artifactsCount = len(artifacts)
        ans = 0
        map = [[[] for _ in range(n)] for _ in range(n)]

        for artifact in artifacts:
            blocks = (artifact[2] - artifact[0] + 1) * (artifact[3] - artifact[1] + 1)
            a = [0, blocks]
            for i in range(artifact[0], artifact[2] + 1):
                for j in range(artifact[1], artifact[3] + 1):
                    map[i][j] = a

        for d in dig:
            temp = map[d[0]][d[1]]
            if temp:
                temp[0] += 1
                if temp[0] == temp[1]:
                    ans += 1

        return ans

test = Solution()
print(test.digArtifacts(
    5,
    [[3,1,4,1],[1,1,2,2],[1,0,2,0],[4,3,4,4],[0,3,1,4],[2,3,3,4]],
    [[0,0],[2,1],[2,0],[2,3],[4,3],[2,4],[4,1],[0,2],[4,0],[3,1],[1,2],[1,3],[3,2]]
))