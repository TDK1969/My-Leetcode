class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def create_tree(nums):
    def dfs(nums, length, index):
        if index < length and nums[index] != -1:
            root = TreeNode(nums[index])
            if 2 * index + 1 < length:
                root.left = dfs(nums, length, 2 * index + 1)
            if 2 * index + 2 < length:
                root.right = dfs(nums, length, 2 * index + 2)
            return root
        return None
    return dfs(nums, len(nums), 0)

def level_order(root):
    res = []
    if not root:
        return res
    queue = [root]
    while queue:
        res.append([])
        temp = []
        for node in queue:
            res[-1].append(node.val)
            if node.left:
                temp.append(node.left)
            if node.right:
                temp.append(node.right)
        queue = temp
    return res

def print_matrix(matrix):
    for row in matrix:
        print("[", end=" ")
        for num in row:
            print(num, end=" ")
        print("]")
