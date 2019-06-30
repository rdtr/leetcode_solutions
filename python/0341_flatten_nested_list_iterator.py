# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """

        self.stack = []
        if not nestedList:
            return

        for nestedInteger in nestedList[::-1]:
            self.stack.append(nestedInteger)

    def next(self):
        """
        :rtype: int
        """

        return self.stack.pop()

    def hasNext(self):
        """
        :rtype: bool
        """

        while self.stack and not self.stack[-1].isInteger():
            nestedList = self.stack.pop().getList()
            for nestedInteger in nestedList[::-1]:
                self.stack.append(nestedInteger)

        return len(self.stack) > 0

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())