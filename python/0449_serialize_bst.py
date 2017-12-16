# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree txo a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "none"
        
        res = ""
        
        stack = []
        cur = root
        while True:
            if not cur:
                break
            res += str(cur.val) + ","
            
            if cur.right:
                stack.append(cur)
            
            if not cur.left:
                if not stack:
                    break
                else:
                    cur = stack.pop()
                    cur = cur.right
            else:
                cur = cur.left
        return res[:-1]
            
            
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "none":
            return None
        vals = data.split(",")
        root = TreeNode(int(vals[0]))
        cur = root
        
        print vals
        i = 1
        stack = []
        while i < len(vals):
            val = int(vals[i])
            
            if val < cur.val:
                cur.left = TreeNode(val)
                stack.append(cur)
                cur = cur.left
            else:
                while cur.val < val:
                    if stack and stack[-1].val < val:
                        cur = stack.pop()
                    else:
                        break
                cur.right = TreeNode(val)
                cur = cur.right
            i += 1
        return root
            
                        
            
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))