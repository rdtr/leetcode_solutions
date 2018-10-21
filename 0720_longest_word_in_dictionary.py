class TrieNode:
    def __init__(self, word='', end=False):
        self.end = end
        self.word = word
        self.children = {}

class Solution:
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        
        # build Trie
        root = TrieNode()
        for word in words:
            cur = root
            for i, ch in enumerate(word):
                if ch in cur.children:
                    cur = cur.children[ch]
                else:
                    nextNode = TrieNode()
                    cur.children[ch] = nextNode
                    cur = nextNode
                if i == len(word) - 1:
                    cur.end = True
                    cur.word = word
        
        # check Trie
        stack = list(root.children.values())
        res = ''
        while stack:
            node = stack.pop(-1)
            if node.end:
                if len(res) < len(node.word) or (len(res) == len(node.word) and res > node.word):
                    res = node.word
                stack.extend(list(node.children.values()))
        return res