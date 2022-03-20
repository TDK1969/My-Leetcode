from typing import List

class Solution:
    def maximumGood(self, statements: List[List[int]]) -> int:
        n = len(statements)
        # assume = [2 for _ in range(n)]
        max1 = 0
        def dfs(p: int, assume: List):
            if p == n:
                nonlocal max1
                max1 = max(sum(assume), max1)
                return
            temp_assume = assume[:]
            if assume[p] == 1:
                # 验证是否符合好人的假设
                for i in range(n):
                    if statements[p][i] == 0 and assume[i] == 1 or statements[p][i] == 1 and assume[i] == 0:
                        return
                # 如果符合，则根据好人的进一步假设
                for i in range(n):
                    if assume[i] == 2:
                        temp_assume[i] = statements[p][i]

                dfs(p + 1, temp_assume)

            if assume[p] == 0:
                # 验证是否说了真话
                flag = 1
                for i in range(n):
                    if statements[p][i] == 0 and assume[i] == 1 or statements[p][i] == 1 and assume[i] == 0:
                        # 有存在说谎
                        flag = 0
                        break
                if flag == 1:
                    temp_assume = assume[:]
                    for i in range(n):
                        if assume[i] == 2:
                            temp_assume[i] = statements[p][i]
                    dfs(p + 1, temp_assume)

                flag = 1
                for i in range(n):
                    if statements[p][i] == 0 and assume[i] == 0 or statements[p][i] == 1 and assume[i] == 1:
                        flag = 0
                        break
                if flag == 0:
                    return
                if flag == 1:
                    temp_assume = assume[:]
                    for i in range(n):
                        if assume[i] == 2 and statements[p][i] != 2:
                            temp_assume[i] =  1 if statements[p][i] == 0 else 0
                    dfs(p + 1, temp_assume)

            if assume[p] == 2:
                flag = 1
                for i in range(n):
                    if statements[p][i] == 0 and assume[i] == 1 or statements[p][i] == 1 and assume[i] == 0:
                        # 有存在说谎
                        flag = 0
                        break
                if flag == 1:
                    temp_assume = assume[:]
                    temp_assume[p] = 1
                    for i in range(n):
                        if assume[i] == 2 and i != p:
                            temp_assume[i] = statements[p][i]
                    dfs(p + 1, temp_assume)

                flag = 1
                for i in range(n):
                    if statements[p][i] == 0 and assume[i] == 0 or statements[p][i] == 1 and assume[i] == 1:
                        flag = 0
                        break
                if flag == 0:
                    return
                if flag == 1:
                    temp_assume = assume[:]
                    temp_assume[p] = 0
                    for i in range(n):
                        if assume[i] == 2 and statements[p][i] != 2 and i != p:
                            temp_assume[i] = 1 if statements[p][i] == 0 else 0
                    dfs(p + 1, temp_assume)

        dfs(0, [2 for _ in range(n)])
        return max1

test = Solution()
print(test.maximumGood(statements = [[2,0,2,2,0],[2,2,2,1,2],[2,2,2,1,2],[1,2,0,2,2],[1,0,2,1,2]]))


