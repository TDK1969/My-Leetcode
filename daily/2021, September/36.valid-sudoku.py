from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        nums1 = set()
        nums2 = set()
        check = [[set() for _ in range(3)] for _ in range(3)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in nums1:
                        return False
                    else:
                        nums1.add(board[i][j])
                    if board[i][j] in check[i // 3][j // 3]:
                        return False
                    else:
                        check[i // 3][j // 3].add(board[i][j])
                if board[j][i] != '.':
                    if board[j][i] in nums2:
                        return False
                    else:
                        nums2.add(board[j][i])
            nums1.clear()
            nums2.clear()
        return True


test = Solution()
print(test.isValidSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."]
                             , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
                             , [".", "9", "8", ".", ".", ".", ".", "6", "."]
                             , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
                             , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
                             , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
                             , [".", "6", ".", ".", ".", ".", "2", "8", "."]
                             , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
                             , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
