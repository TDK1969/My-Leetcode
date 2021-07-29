from typing import List


class Solution:
    class TreeNode:
        def __init__(self, x: int, left: 'Solution.TreeNode' = None, right: 'Solution.TreeNode' = None):
            self.val = x
            self.left = left
            self.right = right

    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:

        global head
        nodes = {}
        n = set()
        for pairs in adjacentPairs:
            val1, val2 = pairs
            if val1 in nodes:
                node1 = nodes[val1]
            else:
                node1 = self.TreeNode(val1)
                nodes[val1] = node1
            if val2 in nodes:
                node2 = nodes[val2]
            else:
                node2 = self.TreeNode(val2)
                nodes[val2] = node2
            n.add(node1)
            n.add(node2)
            head = node1
            if not node1.left:
                node1.left = node2
            else:
                node1.right = node2
            if not node2.left:
                node2.left = node1
            else:
                node2.right = node1
        visited = set()
        while head.left and head.right:
            if head.left not in visited:
                head = head.left
            else:
                head = head.right

        visited.clear()
        ans = []
        while head:
            ans.append(head.val)
            if len(ans) == len(nodes):
                break
            visited.add(head.val)
            if head.left and head.left.val not in visited:
                head = head.left
            elif head.right and head.right.val not in visited:
                head = head.right

        return ans

test = Solution()
print(test.restoreArray([[69922,86539],[-15590,-22801],[72138,-28458],[-15590,-33097],[-28458,19197],[30152,69922],[-33097,-56099],[84189,-22801],[-56099,-58156],[72138,38249],[30152,-81777],[38249,84189],[-55922,19197],[-55922,86539]]))





