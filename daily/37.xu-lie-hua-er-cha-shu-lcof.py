class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def front(self, root, qianxu):
        """

        :type root: TreeNode
        :type qianxu: list
        """
        qianxu.append(root.val)
        if root.left:
            self.front(root.left, qianxu)
        if root.right:
            self.front(root.right, qianxu)

    def middle(self, root, zhongxu):
        """

        :type root: TreeNode
        :type zhongxu: list
        """
        if root.left:
            self.middle(root.left, zhongxu)
        zhongxu.append(root.val)
        if root.right:
            self.middle(root.right, zhongxu)

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        qianxu = []
        zhongxu = []
        self.front(root, qianxu)
        self.middle(root, zhongxu)
        string = ""
        for i in range(len(qianxu)):
            string += str(qianxu[i])
            if i != len(qianxu) - 1:
                string += '#'

        string += '@'

        for i in range(len(zhongxu)):
            string += str(zhongxu[i])
            if i != len(zhongxu[i]):
                string += '#'

        return string

    def buildtree(self, qianxu, zhongxu):
        """

        :type qianxu: list
        :type zhongxu: list
        :rtype: TreeNode
        """
        if zhongxu:
            val = qianxu.pop(0)
            i = zhongxu.index(val)
            left = zhongxu[:i]
            right = zhongxu[i + 1:]

            newnode = TreeNode(val)
            newnode.left = self.buildtree(qianxu, left)
            newnode.right = self.buildtree(qianxu, right)

            return newnode
        return None


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        two = data.split('@')

        qianxu = []
        qian = two[0].split('#')
        for node in qian:
            qianxu.append(int(node))

        zhongxu = []
        zhong = two[1].split('#')
        for node in zhong:
            zhongxu.append(int(node))

        root = self.buildtree(qianxu, zhongxu)
        return root

