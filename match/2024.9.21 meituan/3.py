
class Solution:
    def __init__(self, s: str) -> None:
        # 需要统计最大值的分布
        self.s = list(s)
        self.tree = {}
    

    def build_tree(self) -> None:
        pass

    def replace(self, index: int, p: str) -> None:
        self.s[index - 1] = p
    
    def query(self, left: int, right: int) -> int:
        left -= 1
        right -= 1
        max_shop = max(self.s[left:right+1])
        indexes = []
        for i in range(left, right + 1):
            if self.s[i] == max_shop:
                indexes.append(i)
        

        ans = max(indexes[0] - left, right - indexes[-1])
        for j in range(1, len(indexes)):
            ans = max(ans, (indexes[j] - indexes[j - 1] - 1) // 2)
        return ans

# t = int(input())
# for _ in range(t):
#     n, q = list(map(int, input().split()))
#     s = input()
#     sol = Solution(s)
#     for _ in range(q):
#         op, val1, val2 = input().split()
#         if op == "1":
#             sol.replace(int(val1), val2)
#         elif op == "2":
#             print(sol.query(int(val1), int(val2)))



s = Solution("aazaazaazaa")
print(s.query(1, 11))


# s = Solution("aaaaa")
# print(s.query(1, 4))
# s.replace(2, "f")
# print(s.query(1, 4))
