"""
日期: 2023-09-23
题目: 树上的操作
链接: https://leetcode-cn.com/problems/operations-on-tree/
"""

from typing import *
from collections import *
class LockingTree:

    def __init__(self, parent: List[int]):
        self.n = len(parent)
        self.parent = parent
        self.children = [[] for _ in range(self.n)]
        for i in range(1, self.n):
            self.children[parent[i]].append(i)
        self.lock_dict = {}

    def lock(self, num: int, user: int) -> bool:
        if num not in self.lock_dict:
            self.lock_dict[num] = user
            return True
        else:
            return False


    def unlock(self, num: int, user: int) -> bool:
        if num not in self.lock_dict:
            return False
        elif self.lock_dict[num] != user:
            return False
        else:
            self.lock_dict.pop(num)
            return True


    def upgrade(self, num: int, user: int) -> bool:
        if 0 in self.lock_dict:
            return False

        t = num
        while t != 0:   
            if t in self.lock_dict:
                return False
            t = self.parent[t]
        
        lock_child = []
        
        def dfs(root: int):
            if root in self.lock_dict:
                lock_child.append(root)
            
            for child in self.children[root]:
                dfs(child)

        dfs(num)
        if not lock_child:
            return False
        
        for c in lock_child:
            self.lock_dict.pop(c)
        self.lock_dict[num] = user
        return True


            

        

        
        



# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)