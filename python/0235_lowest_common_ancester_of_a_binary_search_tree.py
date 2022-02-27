class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        x, pok, qok = self.find(root, p, q)
        if x is None:
            return None
        return x

    # find returns three values, x, pok, qok.
    # x returns TreeNode if LCA found, otherwise None.
    # pok returns True if p found among its decendants, otherwise False.
    # qok returns True if q found among its decendants, otherwise False.
    def find(self, parent, p, q):
        if not parent:
            return None, False, False
        if parent == p:
            if p == q:
                return parent, True, True
            # parent is p, check q is found among left subtree or right subtree.
            r, pok1, qok1 = self.find(parent.right, p, q)
            if qok1:
                return parent, True, True
            l, pok2, qok2 = self.find(parent.left, p, q)
            if qok2:
                return parent, True, True
            return None, True, False

        if parent == q:
            if p == q:
                return parent, True, True
            # parent is q, check p is found among left subtree or right subtree.    
            r, pok1, qok1 = self.find(parent.right, p, q)
            if pok1:
                return parent, True, True
            l, pok2, qok2 = self.find(parent.left, p, q)
            if pok2:
                return parent, True, True
            return None, False, True

        # check both right subtree and left subtree
        r, pok1, qok1 = self.find(parent.right, p, q)
        if r:
            return r, True, True
        l, pok2, qok2 = self.find(parent.left, p, q)
        if l:
            return l, True, True
        if (pok1 and qok2) or (
                pok2 and qok1):  # if p and q found on each side, parent is LCA
            return parent, True, True
        return None, pok1 or pok2, qok1 or qok2
