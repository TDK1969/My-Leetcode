"""
日期: 2022-04-13
题目: O(1) 时间插入、删除和获取随机元素
链接: https://leetcode-cn.com/problems/insert-delete-getrandom-o1/
"""
import random
class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.dict = {}


    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        else:
            self.dict[val] = len(self.nums)
            self.nums.append(val)
            return True


    def remove(self, val: int) -> bool:
        if val not in self.dict:
            return False
        else:
            valID = self.dict[val]
            self.nums[valID] = self.nums[self.dict[self.nums[-1]]]
            self.dict[self.nums[-1]] = valID
            del self.dict[val]
            self.nums.pop()
            return True
            
    def getRandom(self) -> int:
        return random.choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()