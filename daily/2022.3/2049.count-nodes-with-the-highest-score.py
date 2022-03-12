from typing import List
class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        if len(parents) == 0:
            return 0
        n = len(parents)
        root = -1
        children = [[] for _ in range(n)]
        for i in range(n):
            if parents[i] != -1:
                children[parents[i]].append(i)
            else:
                root = i
        subTree = [[] for _ in range(n)]

        def dfs(root: int):
            temp = 0
            if children[root]:
                for child in children[root]:
                    sub = dfs(child) + 1
                    temp += sub
                    subTree[root].append(sub)
            return temp
        
        dfs(root)

        count = 0
        maxScore = -1
        for i in range(n):
            subs = sum(subTree[i])
            if subs == 0:
                score = n - 1
            else:
                score = 1
                for j in subTree[i]:
                    score *= j
                score = score * (n - 1 - subs) if subs != n - 1 else score

            if score > maxScore:
                maxScore = score
                count = 1
            elif score == maxScore:
                count += 1

        return count

test = Solution()
print(test.countHighestScoreNodes([]))
