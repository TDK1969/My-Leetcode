class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        node = []
        node_val = []

        node.append(root)
        while node:
            temp_node = node.pop(0)
            if temp_node == None:
                node_val.append(-1005)
            else:
                node_val.append(temp_node.val)
                node.append(temp_node.left)
                node.append(temp_node.right)

            node_string = ""
            for val in node_val:
                node_string += str(val)
                if val != node_val[-1]:
                    node_string += '#'

            return node_string

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        node_val_str = data.split('#')
        node_val_int = []
        for val in node_val_str:
            node_val_int.append(int(val))

        node_val_int.insert(0, None)
        queue = []
        root = None
        if node_val_int[1] != 1005:
            root = TreeNode(node_val_int[1])

        queue.append((root, 1))

        while queue:
            node, index = queue.pop(0)
            pass




