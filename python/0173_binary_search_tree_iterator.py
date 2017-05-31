class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        if not root:
            return
        while True:
            self.stack.append(root)
            if not root.left:
                break
            root = root.left

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack) > 0

    def next(self):
        """
        :rtype: int
        """
        node = self.stack.pop()
        if node.right:
            newnode = node.right
            while True:
                self.stack.append(newnode)
                if not newnode.left:
                    break
                newnode = newnode.left
        return node.val